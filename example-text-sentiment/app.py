#!/usr/bin/env python3
"""
Text Sentiment Analyzer - Command Line Interface

A simple CLI for analyzing text sentiment using HuggingFace models.
"""

import argparse
import sys
from src.sentiment import SentimentAnalyzer


def main():
    """Main function for CLI."""
    parser = argparse.ArgumentParser(
        description="Analyze sentiment of text using AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py --text "I love this!"
  python app.py  (interactive mode)
  
This is an example applet demonstrating the repository structure.
        """
    )
    
    parser.add_argument(
        "--text",
        type=str,
        help="Text to analyze (if not provided, enters interactive mode)"
    )
    
    args = parser.parse_args()
    
    # Initialize the analyzer
    print("=" * 60)
    print("Text Sentiment Analyzer")
    print("=" * 60)
    
    try:
        analyzer = SentimentAnalyzer()
    except Exception as e:
        print(f"\nError initializing model: {e}")
        print("\nMake sure you have installed the requirements:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    
    # Single text analysis mode
    if args.text:
        result = analyzer.analyze(args.text)
        print("\n" + "-" * 60)
        print(f"Input: {args.text}")
        print("-" * 60)
        print(f"Sentiment: {result['label']}")
        print(f"Confidence: {result['score']:.4f}")
        print("-" * 60)
        return
    
    # Interactive mode
    print("\nInteractive Mode - Enter text to analyze (Ctrl+C to exit)")
    print("-" * 60)
    
    try:
        while True:
            text = input("\nEnter text: ").strip()
            
            if not text:
                print("Please enter some text.")
                continue
            
            result = analyzer.analyze(text)
            print(f"\nSentiment: {result['label']}")
            print(f"Confidence: {result['score']:.4f}")
            
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
