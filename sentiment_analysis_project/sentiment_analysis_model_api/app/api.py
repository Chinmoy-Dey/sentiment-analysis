import json
import sys
import os
from typing import Any
from pydantic import BaseModel

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from sentiment_analysis_model.predict import analyze_sentiment

from app.config import settings

api_router = APIRouter()

# Define a Pydantic model for input
class TextInput(BaseModel):
    text: str

@api_router.post("/analyze-sentiment/")
async def analyze_sentiment(input: TextInput):
# Load the model and tokenizer
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
   
    # Define the sentiment analysis pipeline
    sentiment_analysis_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
   
    # Perform sentiment analysis
    result = sentiment_analysis_pipeline(input.text)
    
    # Return the result
    return {"text": input.text, "sentiment": result[0]['label'], "score": result[0]['score']}