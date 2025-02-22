# ComicCrafterAI

ComicCrafterAI is an AI-powered tool that generates comic book-style short stories based on user prompts. The story follows a structured format: Introduction, Storyline, Climax, and Moral of the Story.

[Watch the video in action](https://drive.google.com/file/d/10sXqtuRIOgqaq1R5SjVFH-bGZL-lhYVN/view?usp=sharing)
## Features

- **AI-Generated Stories**: The model generates structured comic book stories alongwith AI generated images.
- **Gradio UI**: A user-friendly interface for easy interaction.
- **OpenAI-Compatible API**: Uses a locally hosted LLM for text generation.
- **Comfy UI**: Uses a locally hosted fine-tuned Stable Diffusion model for image generation.

## System Requirements

- **Processor**: Greater or equivalent to 6 core processor.
- **RAM**: Greater or equivalent of 16GB ram.
- **VRAM**: Greater or equivalent of 4GB vram.
- **Storage**: Greater or equivalent of 256GB storage.
- **Power**: Charger should be plugged in if running on a laptop.

## Installation

### Prerequisites

- Python 3.10+
- Visual Studio Code
- Miniconda
- LM-studio 0.3.8 (build 4)
  ```sh
  https://lmstudio.ai
  ```
- Comfy-UI 0.3.14
  ```sh
  https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#installing
  ```
- Virtual environment (recommended):
  ```sh
  conda create --name myenv python=3.10
  ```
  ```sh
  conda activate myenv
  ```
- Required Python libraries:
  ```sh
  pip install openai==1.61.1
  pip install gradio==5.7.1
  pip install json==2.0.9
  pip install os
  pip install time
  ```
  ```sh
  pip install websocket-client==1.8.0
  pip install urllib==2.2.3
  pip install uuid
  ```

### Setting Up

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/comiccrafterai.git
   cd comiccrafterai
   ```
2. Run the local LLM API via the LM-studio platform:
   ```sh
   1. Download the 'gemma-2-2b-it' model inside the LM-studio.
   2. Go to the Developer options in LM-studio, start the server and load the 'gemma-2-2b-it' model into the memory.
   ```
3. Run the Local image generation model via the Comfy-UI plarform:
   ```sh
   1. Download the Stable Diffusion from this link  'https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt?download=true'
   2. Download the FLUX Model from this link  'https://huggingface.co/city96/FLUX.1-schnell-gguf/resolve/main/flux1-schnell-Q2_K.gguf?download=true'
   3. Move the model to the location 'C:/ComfyUI_windows_portable_nvidia/ComfyUI_windows_portable/ComfyUI/models/checkpoints/'
   4. Download the text encoder from this link  'https://huggingface.co/city96/t5-v1_1-xxl-encoder-gguf/resolve/main/t5-v1_1-xxl-encoder-Q3_K_S.gguf'
   5. Download the clip from this link  'https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors'
   6. Move the text encoder and clip_i to this location 'C:/ComfyUI_windows_portable_nvidia/ComfyUI_windows_portable/ComfyUI/models/clip'
   7. Execute the batch operable 'run_nvidia_gpu.bat' if you have Nvidia GPU of atleast 4GB VRAM.
   8. Execute the batch operable 'run_cpu.bat' if you have do not have the GPU in your system.
5. Launch the Visual Studio Code:
   ```sh
   1. Launch the comic.ipynb jupyter file
   1. Select your newly created environment Cntrl + Shift + P to select your python interpreter.
   2. Execute the each cell to open a Gradio interface in the end.
   3. Note: Make sure to replace your local server ip wherever designated.
   ```

## Usage

1. Automatically Open the Gradio interface in your browser.
2. Enter a prompt describing your comic idea.
3. The AI generates a short story in comic book format.
4. Download or save the generated content.

## API Configuration

The model interacts with an OpenAI-compatible API hosted locally. Modify the API base URL in `comic.ipynb` if necessary:

```python
base_url="http://your-local-server-ip-here/v1"
api_key="lm-studio"
```

## Contributing

Feel free to submit issues and pull requests to improve the project.

## License

This project is licensed under the MIT License.


