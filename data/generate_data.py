import numpy as np
import pandas as pd

# Assuming config.py contains the necessary configurations
exec(open('config.py').read())

def generate_dataset():
    np.random.seed(SEED)
    x1 = np.random.normal(size=DATA_SIZE)
    x2 = np.random.normal(size=DATA_SIZE)
    y = 3 * x1 + 2 * x2 + np.random.normal(size=DATA_SIZE)
    df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})
    return df
