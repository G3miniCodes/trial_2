import config

from data.load_data import load_dataset
from preprocessing.clean_data import clean_data
from preprocessing.feature_engineering import create_features

from models.train_model import train_model
from models.predict_model import make_predictions

from evaluation.metrics import calculate_mse
from evaluation.visualize import plot_results

from utils.logger import log_message

def main():
    log_message("Starting ML Pipeline")

    data = load_dataset()
    clean = clean_data(data)
    features = create_features(clean)
    model = train_model(features)
    pred = make_predictions(model, features)
    score = calculate_mse(pred, features.y)
    plot_results(features.y, pred)
    log_message(f"Final MSE: {score}")

if __name__ == "__main__":
    main()