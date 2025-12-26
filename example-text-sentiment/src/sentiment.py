"""
Sentiment Analysis Module

This module provides a simple interface for sentiment analysis using
HuggingFace Transformers.
"""

from transformers import pipeline


class SentimentAnalyzer:
    """A simple sentiment analyzer using a pre-trained model."""
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initialize the sentiment analyzer.
        
        Args:
            model_name (str): HuggingFace model ID to use
        """
        print(f"Loading model: {model_name}")
        print("(This may take a moment on first run while downloading the model)")
        self.classifier = pipeline("sentiment-analysis", model=model_name)
        print("Model loaded successfully!")
    
    def analyze(self, text):
        """
        Analyze the sentiment of the given text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Dictionary containing 'label' and 'score'
                  label: 'POSITIVE' or 'NEGATIVE'
                  score: Confidence score between 0 and 1
        """
        if not text or not text.strip():
            return {"label": "NEUTRAL", "score": 0.0, "error": "Empty text"}
        
        result = self.classifier(text)[0]
        return result
    
    def analyze_batch(self, texts):
        """
        Analyze sentiment for multiple texts at once.
        
        Args:
            texts (list): List of strings to analyze
            
        Returns:
            list: List of result dictionaries
        """
        if not texts:
            return []
        
        results = self.classifier(texts)
        return results
