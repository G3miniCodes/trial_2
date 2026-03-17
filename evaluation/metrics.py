def calculate_mse(pred, actual):
    mse = ((pred - actual) ** 2).mean()
    return mse
