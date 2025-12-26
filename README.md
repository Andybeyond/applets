# AI-Powered Applets

A collection of AI-powered applets built with free open-source models from HuggingFace and other resources. This repository serves as an ideation and prototyping playground for various AI applications.

## 🎯 Purpose

This repository is designed to host multiple independent AI-powered applets, each serving as a standalone application. Each applet lives in its own subdirectory and can have its own:
- Technology stack
- Dependencies
- Build system
- Documentation
- Testing framework

## 📁 Repository Structure

```
applets/
├── README.md                 # This file
├── .gitignore               # Common ignore patterns for all tech stacks
├── applet-1/                # Example: Sentiment analysis applet
│   ├── README.md            # Applet-specific documentation
│   ├── requirements.txt     # Python dependencies (if Python-based)
│   ├── src/                 # Source code
│   └── ...                  # Other applet-specific files
├── applet-2/                # Example: Image generation applet
│   ├── README.md            # Applet-specific documentation
│   ├── package.json         # Node.js dependencies (if Node-based)
│   ├── src/                 # Source code
│   └── ...                  # Other applet-specific files
└── ...                      # More applets
```

## 🚀 Getting Started

### Exploring Applets

Each applet is completely independent. To use an applet:

1. Navigate to the applet's directory
2. Read the applet's README.md for specific instructions
3. Follow the setup and installation steps provided in that README
4. Run the applet as described in its documentation

### Creating a New Applet

To add a new applet to this repository:

1. **Create a new directory** with a descriptive name:
   ```bash
   mkdir my-new-applet
   cd my-new-applet
   ```

2. **Set up your tech stack** - Choose any technology you prefer:
   - Python (Flask, FastAPI, Streamlit, Gradio, etc.)
   - Node.js (Express, React, Vue, Next.js, etc.)
   - Rust, Go, Ruby, or any other language
   - Any AI/ML framework (Transformers, LangChain, etc.)

3. **Create a README.md** in your applet directory with:
   - Brief description of what the applet does
   - Prerequisites and dependencies
   - Installation instructions
   - Usage instructions
   - Model information (source, license, etc.)
   - Any limitations or known issues

4. **Include a requirements/dependencies file**:
   - `requirements.txt` for Python
   - `package.json` for Node.js
   - `Cargo.toml` for Rust
   - `go.mod` for Go
   - Or equivalent for your chosen stack

5. **Add your source code** organized in a logical structure

6. **Document environment variables** if needed (use `.env.example` files)

## 🔧 Technology Stack Examples

Each applet can use any technology stack. Common choices include:

### Python-based
- **Frameworks**: Streamlit, Gradio, Flask, FastAPI
- **AI Libraries**: Transformers, LangChain, Diffusers, PEFT
- **Models**: HuggingFace models, GGUF models, etc.

### JavaScript/TypeScript-based
- **Frameworks**: Next.js, Express, React, Vue
- **AI Libraries**: Transformers.js, LangChain.js, ONNX Runtime
- **Models**: ONNX models, TensorFlow.js models

### Other Languages
- **Rust**: Candle, Burn, ort
- **Go**: GoML, Gorgonia
- **Any language with AI/ML support**

## 📝 Applet Guidelines

### Isolation
- Each applet should be completely independent
- No shared dependencies between applets at the repository root level
- Each applet manages its own dependencies

### Documentation
- Every applet must have its own README.md
- Document the AI model(s) used and their sources
- Include setup and usage instructions
- Note any API keys or credentials needed (never commit these!)

### Models and Resources
- Prefer free, open-source models from HuggingFace, GGUF, or similar
- Document model licenses and attribution
- Consider model size and download times
- Provide alternatives when possible

### Git Practices
- The root `.gitignore` covers common patterns for all tech stacks
- Add applet-specific ignores if needed
- Don't commit large model files (use download scripts or document model acquisition)
- Don't commit API keys, credentials, or sensitive data

## 🤝 Contributing

This is a personal ideation and prototyping playground, but contributions or suggestions are welcome! Feel free to:
- Open issues for bugs or suggestions
- Submit pull requests with improvements
- Share ideas for new applets

## 📄 License

Each applet may have its own license based on the models and libraries it uses. Refer to individual applet READMEs for license information.

## 🔗 Resources

- [HuggingFace Models](https://huggingface.co/models)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [LangChain Documentation](https://python.langchain.com/)
- [Gradio Documentation](https://gradio.app/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Happy prototyping! 🚀** 
