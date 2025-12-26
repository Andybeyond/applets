# Quick Start Guide

Welcome to the AI-Powered Applets repository! This is a quick reference to get you started.

## 🎯 What is this repo?

A collection of **independent AI-powered applets**, each in its own directory with its own tech stack. Think of it as a playground for AI experimentation and prototyping.

## 📂 Repository Layout

```
applets/
├── README.md              ← Full documentation (you are here!)
├── CONTRIBUTING.md        ← Detailed guide for adding applets
├── QUICK_START.md         ← This file
├── .gitignore            ← Ignore patterns for all tech stacks
├── .github/
│   └── APPLET_TEMPLATE/  ← Templates for new applets
└── [applet directories]  ← Individual applets go here
```

## 🚀 I want to use an applet

1. Browse the repository for available applets
2. Enter the applet's directory: `cd [applet-name]`
3. Read that applet's README.md
4. Follow its installation and usage instructions

## 🛠️ I want to create a new applet

### Quick Method (5 minutes)

1. **Copy the template**:
   ```bash
   cp -r .github/APPLET_TEMPLATE my-applet-name
   cd my-applet-name
   ```

2. **Edit README.md**: Replace all `[placeholders]` with your info

3. **Set up your tech stack**:
   - Python: Edit `requirements.txt`, delete `package.json`
   - Node.js: Edit `package.json`, delete `requirements.txt`
   - Other: Create appropriate dependency files

4. **Write your code** in a logical structure (see template GUIDE.md)

5. **Test thoroughly** before committing

### Detailed Method

Follow the comprehensive guide in [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📋 Applet Checklist

Every applet should have:
- ✅ Its own directory at repo root
- ✅ A comprehensive README.md
- ✅ Dependency file (requirements.txt, package.json, etc.)
- ✅ Organized source code structure
- ✅ Model attribution and license info
- ✅ Clear installation and usage instructions

## 🎨 Choose Your Stack

You can use **any technology**:
- **Python**: Transformers, LangChain, Streamlit, Gradio, Flask, FastAPI
- **JavaScript/Node.js**: Transformers.js, Next.js, Express, React
- **Rust**: Candle, Burn, ort
- **Go**: GoML, Gorgonia
- **Any other language with AI/ML support!**

## 🤖 Finding Models

- [HuggingFace Models](https://huggingface.co/models) - Thousands of open models
- [HuggingFace Spaces](https://huggingface.co/spaces) - Live demos for inspiration
- [GGUF Models](https://huggingface.co/models?library=gguf) - Quantized models
- [Papers with Code](https://paperswithcode.com/) - Research papers with implementations

## 💡 Applet Ideas

Not sure what to build? Try:

**Easy**:
- Sentiment analyzer (classify text as positive/negative)
- Text summarizer (condense long text)
- Image classifier (identify objects in photos)

**Medium**:
- Chatbot (conversational AI)
- Image caption generator (describe images)
- Text-to-speech converter

**Advanced**:
- Image generator (text-to-image)
- Code assistant (help with programming)
- Multi-modal Q&A (answer questions about images)

## ⚠️ Important Rules

**DO**:
- ✅ Keep each applet completely isolated
- ✅ Use free, open-source models
- ✅ Document everything clearly
- ✅ Use `.env` for secrets (and `.env.example` as template)

**DON'T**:
- ❌ Commit API keys or secrets
- ❌ Commit large model files (provide download instructions)
- ❌ Commit `node_modules/`, `venv/`, or build artifacts
- ❌ Create dependencies between applets

## 📚 More Resources

- **Full docs**: [README.md](./README.md)
- **Contributing guide**: [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Template guide**: [.github/APPLET_TEMPLATE/GUIDE.md](./.github/APPLET_TEMPLATE/GUIDE.md)

## 🆘 Need Help?

- Check existing applets for examples (when available)
- Read the detailed docs
- Open an issue with your question

---

**Ready to build? Copy the template and start coding!** 🚀
