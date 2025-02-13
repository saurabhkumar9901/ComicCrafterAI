# ComicCrafterAI

ComicCrafterAI is an AI-powered tool that generates comic book-style short stories based on user prompts. The story follows a structured format: Introduction, Storyline, Climax, and Moral of the Story.

## Features

- **AI-Generated Stories**: The model generates structured comic book stories alongwith AI generated images.
- **Gradio UI**: A user-friendly interface for easy interaction.
- **OpenAI-Compatible API**: Uses a locally hosted LLM for text generation.
- **Comfy UI**: Uses a locally hosted fine-tuned Stable Diffusion model for image generation.

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
3. Run the Local Stable Diffusion model via the Comfy-UI plarform:
   ```sh
   1. Execute the batch operable 'run_nvidia_gpu.bat' if you have Nvidia GPU of atleast 4GB VRAM.
   2. Execute the batch operable 'run_cpu.bat' if you have do not have the GPU in your system.
5. Launch the Visual Studio Code:
   ```sh
   1. Select your newly created environment Cntrl + Shift + P to select your python interpreter.
   2. Execute the each cell you view the output
   3. Make sure to replace your local server ip wherever designated.
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


