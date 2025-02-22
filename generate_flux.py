#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

def generate_flux_schnell(message):
    def queue_prompt(prompt):
        p = {"prompt": prompt, "client_id": client_id}
        data = json.dumps(p).encode('utf-8')
        req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
        return json.loads(urllib.request.urlopen(req).read())

    def get_image(filename, subfolder, folder_type):
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
            return response.read()

    def get_history(prompt_id):
        with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
            return json.loads(response.read())

    def get_images(ws, prompt):
        prompt_id = queue_prompt(prompt)['prompt_id']
        output_images = {}
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message['type'] == 'executing':
                    data = message['data']
                    if data['node'] is None and data['prompt_id'] == prompt_id:
                        break #Execution is done
            else:
                # If you want to be able to decode the binary stream for latent previews, here is how you can do it:
                # bytesIO = BytesIO(out[8:])
                # preview_image = Image.open(bytesIO) # This is your preview in PIL image format, store it in a global
                continue #previews are binary data

        history = get_history(prompt_id)[prompt_id]
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            images_output = []
            if 'images' in node_output:
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'])
                    images_output.append(image_data)
            output_images[node_id] = images_output

        return output_images

    prompt_text = """
    {
      "3": {
        "inputs": {
          "seed": 312120815043472,
          "steps": 5,
          "cfg": 1,
          "sampler_name": "euler",
          "scheduler": "simple",
          "denoise": 1,
          "model": [
            "31",
            0
          ],
          "positive": [
            "6",
            0
          ],
          "negative": [
            "26",
            0
          ],
          "latent_image": [
            "5",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "5": {
        "inputs": {
          "width": 512,
          "height": 512,
          "batch_size": 1
        },
        "class_type": "EmptyLatentImage",
        "_meta": {
          "title": "Empty Latent Image"
        }
      },
      "6": {
        "inputs": {
          "text": "Comic art styleA grand piano floating serenely in the ocean, where a mermaid plays enchanting melodies, surrounded by bioluminescent creatures.",
          "clip": [
            "34",
            0
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode Positive (Prompt)"
        }
      },
      "8": {
        "inputs": {
          "samples": [
            "3",
            0
          ],
          "vae": [
            "25",
            0
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "9": {
        "inputs": {
          "filename_prefix": "ComfyUI",
          "images": [
            "8",
            0
          ]
        },
        "class_type": "SaveImage",
        "_meta": {
          "title": "Save Image"
        }
      },
      "25": {
        "inputs": {
          "vae_name": "ae.safetensors"
        },
        "class_type": "VAELoader",
        "_meta": {
          "title": "Load VAE"
        }
      },
      "26": {
        "inputs": {
          "text": "Low resolution, blurry, pixelated, oversimplified, generic,Unnatural, unrealistic, exaggerated features, distorted anatomy,Cartoonish, amateurish, simplistic, over-the-top,No text, no watermarks, no logos, no unrealistic textures,No dark, no gloomy, no messy, no chaotic,No overly large eyes, no distorted limbs, no unnatural hair.",
          "clip": [
            "34",
            0
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode Negetive (Prompt)"
        }
      },
      "31": {
        "inputs": {
          "unet_name": "flux1-schnell-Q2_K.gguf"
        },
        "class_type": "UnetLoaderGGUF",
        "_meta": {
          "title": "Unet Loader (GGUF)"
        }
      },
      "34": {
        "inputs": {
          "clip_name1": "t5-v1_1-xxl-encoder-Q3_K_S.gguf",
          "clip_name2": "clip_l.safetensors",
          "type": "flux"
        },
        "class_type": "DualCLIPLoaderGGUF",
        "_meta": {
          "title": "DualCLIPLoader (GGUF)"
        }
      }
    }
    """

    prompt = json.loads(prompt_text)
    #set the text prompt for our positive CLIPTextEncode
    prompt["6"]["inputs"]["text"] = f"Generate a comic art image of the following context : {message}"
    #set the text prompt for our negetive CLIPTextEncode
    prompt["26"]["inputs"]["text"] = "Low resolution, blurry, pixelated, oversimplified, generic,Unnatural, unrealistic, exaggerated features, distorted anatomy,Cartoonish, amateurish, simplistic, over-the-top,No text, no watermarks, no logos, no unrealistic textures,No dark, no gloomy, no messy, no chaotic,No overly large eyes, no distorted limbs, no unnatural hair."
    #set the seed for our KSampler node
    prompt["3"]["inputs"]["seed"] = 5

    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    ws.close() # for in case this example is used in an environment where it will be repeatedly called, like in a Gradio app. otherwise, you'll randomly receive connection timeouts
    #Commented out code to display the output images:

    for node_id in images:
        for image_data in images[node_id]:
            from PIL import Image
            import io
            return(Image.open(io.BytesIO(image_data)))

