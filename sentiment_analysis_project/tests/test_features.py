
"""
Note: These tests will fail if you have not first trained the model.
"""

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np


def test_sample_senntence(sample_input_data):
    # When
    subject = sample_input_data

    # Then
    assert result[0]['label'] == 'POSITIVE'


