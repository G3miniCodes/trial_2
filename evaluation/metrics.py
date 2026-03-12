import numpy as np

def calculate_mse(pred, actual):
    mse = np.mean((pred - actual)**2)
    return mse
