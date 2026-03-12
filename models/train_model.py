import config
import statsmodels.api as sm

def train_model(data):
    if config.MODEL_TYPE == "linear_regression":
        model = sm.OLS(data['y'], sm.add_constant(data.drop(columns=['y']))).fit()
    return model
