"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import pytest
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sentiment_analysis_model.predict import analyze_sentiment

@pytest.fixture
def positive_sentiment():
  return "Positive News is a constructive journalism media brand.We love positive News"

@pytest.fixture
def negative_sentiment():
  return "This assignment was tough as there are many open pieces to make it work together!"

def test_negative_sentiment(negative_sentiment):
  result = analyze_sentiment(negative_sentiment)
  assert result['sentiment'] == 'NEGATIVE'


def test_positive_sentiment(positive_sentiment):
  result = analyze_sentiment(positive_sentiment)
  assert result['sentiment']  == 'POSITIVE'
