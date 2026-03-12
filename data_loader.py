import numpy as np
import pandas as pd
import utils


def load_data():
    print("Loading synthetic dataset...")
    
    x = np.random.normal(size=100)
    y = 2 * x + np.random.normal(size=100)
    
    data = pd.DataFrame({'x': x, 'y': y})
    
    utils.log_message("Data loaded successfully")
    
    return data
