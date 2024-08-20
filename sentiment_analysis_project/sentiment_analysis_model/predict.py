import sys
from pathlib import Path
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch



def analyze_sentiment(text: str):
    # Load the model and tokenizer
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
   
    # Define the sentiment analysis pipeline
    sentiment_analysis_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
   
    # Perform sentiment analysis
    result = sentiment_analysis_pipeline(text)
    
    # Return the result
    return {"text": text, "sentiment": result[0]['label'], "score": result[0]['score']}


if __name__ == "__main__":
    # Test the function with a sample text
    sample_text = "I love this assignemt!"
    output = analyze_sentiment(sample_text)
    print (output)