# VisionGen AI — Generative AI for Computer Vision

A presentation-ready Generative AI + Computer Vision project that demonstrates **text-to-image generation** using a pretrained Stable Diffusion model through Hugging Face Diffusers.

## Project Overview

**VisionGen AI** converts a natural-language prompt into a synthetic image. It provides a simple Streamlit interface where users can enter a prompt, adjust generation settings, and save the generated image.

### Key Concepts Demonstrated

- Generative AI
- Computer Vision
- Diffusion models
- Text-to-image synthesis
- Latent-space generation
- Prompt engineering
- Pretrained deep learning models
- Streamlit deployment

## Architecture

```text
User Prompt
    |
    v
Streamlit Web Interface
    |
    v
Diffusers Text-to-Image Pipeline
    |
    v
Stable Diffusion Model
    |
    v
Generated Image
    |
    +----> Preview
    |
    +----> Download
```

## Features

- Text-to-image generation
- Adjustable image dimensions
- Adjustable inference steps
- Seed control for reproducibility
- GPU/CPU detection
- Download generated images
- Simple presentation-friendly UI

## Project Structure

```text
VisionGenAI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── assets/
│   └── .gitkeep
└── generated/
    └── .gitkeep
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/VisionGenAI.git
cd VisionGenAI
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Hardware

A CUDA-enabled NVIDIA GPU is recommended for practical generation speed. CPU execution is supported but can be significantly slower.

## Example Prompts

- `A futuristic smart city at sunset, cinematic computer vision laboratory`
- `A robot analyzing traffic using computer vision, realistic photography`
- `An autonomous car navigating a rainy city street, detailed digital art`
- `A microscope view of colorful biological cells, scientific visualization`

## How It Works

Stable Diffusion is a diffusion-based generative model. During training, images are progressively corrupted with noise and the model learns to reverse that process. During generation, a text prompt conditions the denoising process so that random latent noise is transformed into an image matching the prompt.

The application uses the Hugging Face Diffusers pipeline instead of implementing the diffusion algorithm from scratch.

## Important Academic Note

This project uses a pretrained generative model for demonstration. It is intended as a **Computer Vision course project/presentation**, not as a claim that the model was trained from scratch.

## Suggested Presentation Flow

1. What is Generative AI?
2. Traditional Computer Vision vs Generative Vision
3. What are diffusion models?
4. Stable Diffusion architecture at a high level
5. Project architecture
6. Live text-to-image demo
7. Prompt engineering examples
8. Applications
9. Limitations and ethical considerations
10. Future enhancements

## Future Enhancements

- Image-to-image generation
- Image captioning
- Object detection on generated images
- ControlNet-based structural control
- LoRA fine-tuning on a custom dataset
- Automatic prompt enhancement
- Generation history dashboard
- Cloud deployment

## Disclaimer

Generated images may contain artifacts, biases, or inaccurate visual details. Model usage must follow the license and usage conditions of the selected pretrained checkpoint.


## 🎓 Viva Questions

### 1. What is Generative AI?
Generative AI creates new content such as images, text, audio, or video by learning patterns from training data.

### 2. What is a diffusion model?
A diffusion model learns to generate data by learning how to reverse a gradual noise-adding process.

### 3. What is Stable Diffusion?
Stable Diffusion is a latent diffusion text-to-image model that generates images from natural-language prompts.

### 4. Why is this a Computer Vision project?
The project operates on visual data and demonstrates image synthesis, visual representation learning, and image generation.

### 5. What is prompt engineering?
Prompt engineering is the process of designing effective textual instructions to guide a generative model toward a desired output.

### 6. What are the limitations?
Outputs can contain artifacts, biased representations, incorrect details, and inconsistent results. Generation speed also depends heavily on available hardware.
