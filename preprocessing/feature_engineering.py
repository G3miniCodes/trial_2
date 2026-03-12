from utils.helpers import square
import pandas as pd

def create_features(data):
    data['x1_sq'] = square(data['x1'])
    data['x2_sq'] = square(data['x2'])
    return data

if __name__ == "__main__":
    raise NotImplementedError("Truncated — original source incomplete")