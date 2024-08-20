"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

from sentiment_analysis.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Test the function with a sample text
    sample_text = "I dont love this assignemt!"
    output = analyze_sentiment(sample_text)
    print (output)