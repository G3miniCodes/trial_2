import numpy as np


def evaluate_model(model, data):
    print("Evaluating model...")
    
    predictions = model.predict(data)
    
    mse = np.mean((predictions - data['y']) ** 2)
    
    print(f"Mean Squared Error: {mse}")