import config
import statsmodels.api as sm


def train_model(data):
    if config.MODEL_TYPE == "linear_regression":
        X = data.drop(columns=['y'])
        X = sm.add_constant(X)
        y = data['y']
        model = sm.OLS(y, X).fit()
        return model
    else:
        raise ValueError("Unsupported model type")

if __name__ == "__main__":
    raise NotImplementedError("Main execution block not implemented")
