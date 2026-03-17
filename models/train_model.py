import config
import statsmodels.api as sm

MODEL_TYPE = 'linear_regression'  # Assuming MODEL_TYPE is defined in config

def train_model(data):
    if MODEL_TYPE == 'linear_regression':
        model = sm.OLS(data['y'], data.drop(columns=['y'])).fit()
    return model
