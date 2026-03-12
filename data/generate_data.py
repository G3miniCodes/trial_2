import numpy as np
import pandas as pd
import config

SEED = config.SEED
DATA_SIZE = config.DATA_SIZE


def generate_dataset():
    np.random.seed(SEED)

    x1 = np.random.normal(size=DATA_SIZE)
    x2 = np.random.normal(size=DATA_SIZE)

    y = 3 * x1 + 2 * x2 + np.random.normal(size=DATA_SIZE)

    df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})

    return df

if __name__ == "__main__":
    df = generate_dataset()
    print(df.head())
