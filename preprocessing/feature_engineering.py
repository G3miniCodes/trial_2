import pandas as pd
from utils.helpers import square

def create_features(data):
    data['x1_sq'] = square(data['x1'])
    data['x2_sq'] = square(data['x2'])
    return data

if __name__ == "__main__":
    raise NotImplementedError("Main execution block not provided")