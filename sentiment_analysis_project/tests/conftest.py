import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import pytest
from sklearn.model_selection import train_test_split

from sentiment_analysis_model.config.core import config
from sentiment_analysis_model.processing.data_manager import load_dataset


@pytest.fixture
def sample_input_data():
    # Test the function with a sample text
    sample_text = "I love this assignemt !"
    print (sample_text)
    return sample_text