# Text Sentiment Analyzer

A simple sentiment analysis applet that classifies text as positive, negative, or neutral using a pre-trained model from HuggingFace.

> **Note**: This is an example applet demonstrating the structure and conventions used in this repository. It serves as a reference for creating your own applets.

## 📖 Description

This applet uses a lightweight sentiment analysis model to analyze the emotional tone of text input. It's perfect for:
- Analyzing customer feedback
- Monitoring social media sentiment
- Understanding text tone
- Learning about HuggingFace Transformers

## 🤖 Model Information

- **Model**: [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- **Source**: HuggingFace
- **License**: Apache 2.0
- **Model Size**: ~255MB
- **Task Type**: Text Classification (Sentiment Analysis)

## 🔧 Prerequisites

- Python 3.8 or higher
- 2GB RAM minimum
- Internet connection for initial model download

## 📦 Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/Andybeyond/applets.git
   cd applets/example-text-sentiment
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Command Line Interface

Run the applet with:

```bash
python app.py --text "I love this repository! It's so helpful."
```

Or use interactive mode:

```bash
python app.py
```

Then enter your text when prompted.

### Python API

You can also use it programmatically:

```python
from src.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()
result = analyzer.analyze("This is an amazing day!")
print(result)
# Output: {'label': 'POSITIVE', 'score': 0.9998}
```

## 💡 Examples

### Example 1: Positive Sentiment

**Input:**
```
I love this repository! It's so helpful and well-organized.
```

**Output:**
```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

### Example 2: Negative Sentiment

**Input:**
```
This is frustrating and doesn't work as expected.
```

**Output:**
```json
{
  "label": "NEGATIVE",
  "score": 0.9995
}
```

## 🏗️ Project Structure

```
example-text-sentiment/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── app.py                # Main CLI application
└── src/
    ├── __init__.py
    └── sentiment.py      # Sentiment analysis logic
```

## ⚙️ Configuration

The model is downloaded automatically on first run and cached locally. By default, it's stored in your HuggingFace cache directory (`~/.cache/huggingface/`).

## ⚠️ Limitations

- **Language**: Primarily trained on English text
- **Length**: Works best with sentences/short paragraphs (not long documents)
- **Domain**: Trained on movie reviews, may not generalize perfectly to all domains
- **Binary**: Only detects positive/negative (no neutral option with this specific model)
- **Context**: May miss sarcasm or complex sentiment expressions

## 🔒 Privacy and Security

- All processing is done locally on your machine
- No data is sent to external services (except initial model download)
- No data is stored or logged

## 🐛 Troubleshooting

### Issue: "No module named 'transformers'"

**Solution**: Make sure you've activated your virtual environment and installed dependencies:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: Slow first run

**Solution**: The model needs to be downloaded on first run (~255MB). This is a one-time operation.

### Issue: Out of memory

**Solution**: This lightweight model should run on most systems, but if you encounter memory issues, close other applications or try on a machine with more RAM.

## 📄 License

This applet uses the DistilBERT model which is licensed under Apache 2.0. The code in this directory is also provided under the Apache 2.0 license.

## 🙏 Acknowledgments

- Model by: HuggingFace team
- Framework: [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- Base model: [DistilBERT](https://arxiv.org/abs/1910.01108)

## 📞 Support

For issues or questions:
- Open an issue in the [main repository](https://github.com/Andybeyond/applets/issues)
- Check the [CONTRIBUTING.md](../CONTRIBUTING.md) for more guidance

---

Built as an example for the [AI-Powered Applets](https://github.com/Andybeyond/applets) collection.
