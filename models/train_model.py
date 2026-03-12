import config
import statsmodels.api as sm

MODEL_TYPE = 'linear_regression'  # This should be set according to your config

def train_model(data):
    if MODEL_TYPE == 'linear_regression':
        X = data.drop(columns=['y'])
        X = sm.add_constant(X)
        y = data['y']
        model = sm.OLS(y, X).fit()
        return model
    else:
        raise ValueError(f"Unsupported model type: {MODEL_TYPE}")

# Example usage
if __name__ == '__main__':
    import pandas as pd
    # Example data
    data = pd.DataFrame({
        'y': [1, 2, 3, 4, 5],
        'x1': [1, 2, 3, 4, 5],
        'x2': [5, 4, 3, 2, 1]
    })
    model = train_model(data)
    print(model.summary())