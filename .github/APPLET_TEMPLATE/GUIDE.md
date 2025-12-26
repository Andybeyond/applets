# Applet Template Guide

This directory contains templates and examples for creating new applets in this repository.

## 📁 What's Included

- **README.md**: A comprehensive template for documenting your applet
- **requirements.txt**: Example Python dependencies file
- **package.json**: Example Node.js dependencies file
- **.env.example**: Template for environment variables

## 🚀 Quick Start

1. **Copy the template** to your new applet directory:
   ```bash
   # From the repository root
   cp -r .github/APPLET_TEMPLATE my-new-applet
   cd my-new-applet
   ```

2. **Choose your stack** and keep only relevant files:
   - For Python: Keep `requirements.txt`, remove `package.json`
   - For Node.js: Keep `package.json`, remove `requirements.txt`
   - For other languages: Create equivalent dependency files

3. **Edit README.md**:
   - Replace all `[placeholders]` with actual information
   - Remove sections that don't apply to your applet
   - Add sections specific to your use case

4. **Set up dependencies**:
   - Edit your chosen dependency file (requirements.txt or package.json)
   - Uncomment and modify the packages you need
   - Add any additional packages specific to your project

5. **Configure environment variables**:
   - Edit `.env.example` with the variables your applet needs
   - Document what each variable is for in comments
   - Create your actual `.env` file (never commit this!)

6. **Start coding**:
   - Create your source code structure (see suggested structure below)
   - Implement your applet functionality
   - Test thoroughly

## 📂 Suggested Project Structure

### Python-based Applet
```
my-python-applet/
├── README.md
├── requirements.txt
├── .env.example
├── app.py                 # Main entry point
├── src/
│   ├── __init__.py
│   ├── model.py           # Model loading and inference
│   ├── utils.py           # Helper functions
│   └── config.py          # Configuration handling
├── scripts/
│   └── download_model.py  # Script to download model
├── tests/
│   ├── __init__.py
│   └── test_app.py
└── docs/
    └── screenshots/
```

### Node.js-based Applet
```
my-nodejs-applet/
├── README.md
├── package.json
├── .env.example
├── src/
│   ├── index.js           # Main entry point
│   ├── model.js           # Model handling
│   ├── routes/            # Express routes (if web app)
│   │   └── api.js
│   └── utils/
│       └── helpers.js
├── public/                # Static files (if web app)
│   ├── index.html
│   └── styles.css
└── tests/
    └── app.test.js
```

### Minimal Applet (any language)
```
my-minimal-applet/
├── README.md
├── [dependency-file]
├── .env.example
├── main.[ext]             # Main application file
└── utils.[ext]            # Helper functions
```

## ✏️ Customization Tips

### README Customization
- **Keep it clear**: Write for someone who's never seen your applet before
- **Be specific**: Include exact commands, not just general instructions
- **Show examples**: Real examples help users understand what to expect
- **Document everything**: Prerequisites, limitations, troubleshooting

### Dependency Management
- **Pin versions**: Use specific versions for stability
- **Minimize dependencies**: Only include what you actually use
- **Document extras**: If some dependencies are optional, note that
- **Consider size**: Be mindful of large dependencies

### Environment Variables
- **Security first**: Never commit secrets or API keys
- **Provide defaults**: Use sensible defaults when possible
- **Document clearly**: Explain what each variable does
- **Validate inputs**: Check environment variables at startup

## 🎯 Best Practices

1. **Test from scratch**: Before committing, test your applet on a fresh clone
2. **Update as you go**: Keep your README updated as your applet evolves
3. **Error handling**: Provide helpful error messages
4. **Resource cleanup**: Clean up models/resources when done
5. **Documentation**: Comment complex logic in your code

## 📚 Additional Resources

- See [CONTRIBUTING.md](../../CONTRIBUTING.md) for detailed guidelines
- Check out [README.md](../../README.md) for repository overview
- Browse existing applets for inspiration and patterns

## 💡 Need Help?

- Review existing applets in the repository for examples
- Check the main CONTRIBUTING.md for more detailed guidance
- Open an issue if you have questions

---

Happy building! 🎉
