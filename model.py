import statsmodels.formula.api as smf


def train_model(data):
    print("Training Linear Regression Model...")
    
    model = smf.ols(formula='y ~ x', data=data).fit()
    
    return model
