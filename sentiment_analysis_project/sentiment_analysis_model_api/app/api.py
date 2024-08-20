import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sentiment_analysis_model import __version__ as model_version
from sentiment_analysis_model.predict import analyze_sentiment

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()

@api_router.post("/analyze-sentiment/")
async def analyze_sentiment(input: TextInput):
    # Perform sentiment analysis
    result = analyze_sentiment(input.text)
    
    # Return the result
    return {"text": input.text, "sentiment": result[0]['label'], "score": result[0]['score']}
