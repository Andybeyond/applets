# Contributing to AI-Powered Applets

Thank you for your interest in contributing to this repository! This document provides guidelines for adding new applets or improving existing ones.

## 🎯 Philosophy

This repository is designed as an **ideation and prototyping playground** where each applet is:
- **Independent**: Complete isolation from other applets
- **Experimental**: Prioritize rapid prototyping over production-readiness
- **Educational**: Learn and explore AI capabilities
- **Open-source**: Use free, open-source models and tools

## 📋 Applet Requirements

### Mandatory

Every applet **must** have:

1. **Its own directory** at the root level with a descriptive name (e.g., `sentiment-analyzer`, `image-captioning`)

2. **A comprehensive README.md** including:
   - Clear description of what the applet does
   - Prerequisites (Python version, Node version, etc.)
   - Installation instructions (step-by-step)
   - Usage instructions with examples
   - Model information:
     - Model name and source (e.g., HuggingFace model ID)
     - Model license
     - Model size and system requirements
   - Any limitations or known issues
   - Attribution for models and libraries used

3. **Dependency management file**:
   - `requirements.txt` for Python projects
   - `package.json` for Node.js projects
   - Equivalent for other languages
   - Pin versions when stability is important

4. **Source code** organized logically:
   ```
   my-applet/
   ├── README.md
   ├── requirements.txt or package.json
   ├── src/              # Source code
   ├── tests/            # Tests (optional but encouraged)
   ├── .env.example      # Example environment variables
   └── scripts/          # Helper scripts (optional)
   ```

### Recommended

For better applets, consider adding:

- **Tests**: Basic tests to verify functionality
- **Examples**: Sample inputs and expected outputs
- **.env.example**: Template for environment variables (never commit actual .env)
- **Docker support**: Dockerfile for containerized deployment
- **License file**: If the applet has specific licensing requirements
- **Screenshots**: Visual examples of the applet in action
- **Requirements documentation**: Hardware requirements (GPU, RAM, etc.)

## 🔧 Technology Stack Guidelines

### Choose Freely
- Use **any** programming language or framework
- Select the **best tool** for your specific use case
- Don't worry about consistency with other applets

### Prefer Open Source
- Use free, open-source models from HuggingFace, GGUF repositories, or similar
- Document model sources and licenses
- Avoid proprietary or paid APIs when possible (but document if used)

### Consider Accessibility
- Document system requirements clearly
- Provide lighter model alternatives when possible
- Consider download times for large models
- Offer options to download models vs. using hosted APIs

## 🚫 What NOT to Commit

Never commit:
- **API keys or secrets**: Use environment variables
- **Large model files**: Provide download scripts or instructions instead
- **Generated outputs**: Unless they're example outputs for documentation
- **Personal data**: No real user data or sensitive information
- **Dependencies**: Don't commit `node_modules/`, `venv/`, etc.
- **Build artifacts**: These are in .gitignore

## 📝 Creating a New Applet: Step-by-Step

### 1. Plan Your Applet
- Define a clear, focused purpose
- Choose your AI model(s)
- Select your technology stack
- Verify the model is open-source and accessible

### 2. Set Up the Directory
```bash
# Create applet directory
mkdir my-awesome-applet
cd my-awesome-applet

# Initialize your project
# For Python:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install transformers torch

# For Node.js:
npm init -y
npm install @huggingface/transformers

# For other stacks:
# Follow standard initialization for your chosen technology
```

### 3. Create the README
Use this template:

```markdown
# Applet Name

Brief one-line description.

## Description

Detailed description of what this applet does and why it's useful.

## Model Information

- **Model**: [model-name](https://huggingface.co/model-path)
- **Source**: HuggingFace / Other
- **License**: MIT / Apache 2.0 / etc.
- **Size**: ~500MB
- **Task**: Text classification / Image generation / etc.

## Prerequisites

- Python 3.8+ / Node.js 16+ / etc.
- 4GB RAM minimum
- (Optional) CUDA-capable GPU for faster inference

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Andybeyond/applets.git
   cd applets/my-awesome-applet
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   npm install
   ```

3. (Optional) Download model:
   ```bash
   python download_model.py
   ```

## Usage

Describe how to run the applet:

```bash
python app.py
# or
npm start
```

Then open http://localhost:3000 in your browser.

### Examples

Provide usage examples with sample inputs and outputs.

## Limitations

- List any known limitations
- Performance considerations
- Compatibility issues

## License

[Specify license based on model and dependencies]

## Attribution

Credit the model creators and any significant libraries used.
```

### 4. Develop Your Applet
- Write clean, well-commented code
- Handle errors gracefully
- Provide helpful error messages
- Test your applet thoroughly

### 5. Document Everything
- Update your README as you develop
- Add inline comments for complex logic
- Create a .env.example if you use environment variables
- Document any non-obvious setup steps

### 6. Test Before Committing
- Test installation from scratch
- Verify all instructions in your README work
- Test on different systems if possible
- Ensure no secrets are in your code

### 7. Commit and Push
```bash
git add my-awesome-applet/
git commit -m "Add my-awesome-applet: brief description"
git push
```

## 💡 Applet Ideas

Need inspiration? Consider these categories:

### Text Processing
- Sentiment analysis
- Text summarization
- Translation
- Named entity recognition
- Text generation
- Question answering

### Image Processing
- Image classification
- Object detection
- Image captioning
- Image generation
- Style transfer
- Image segmentation

### Audio Processing
- Speech-to-text
- Text-to-speech
- Music generation
- Audio classification
- Voice cloning

### Multimodal
- Visual question answering
- Image-to-text and text-to-image
- Video understanding
- Document understanding

### Fun Projects
- Chatbots
- Story generators
- Code assistants
- Meme generators
- Style transfer apps

## 🐛 Issues and Improvements

### Reporting Issues
- Check if an issue already exists
- Provide clear reproduction steps
- Include your environment details
- Share error messages and logs

### Suggesting Improvements
- Describe the improvement clearly
- Explain the benefit
- Consider backwards compatibility
- Be open to discussion

## 📞 Questions?

Feel free to:
- Open an issue for questions
- Start a discussion
- Reach out to the repository owner

---

Happy building! 🎉
