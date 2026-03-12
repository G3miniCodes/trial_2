import pandas as pd


def normalize(column):
    return (column - column.min()) / (column.max() - column.min())


def preprocess_data(data):
    print("Preprocessing data...")
    data['x'] = normalize(data['x'])
    return data


if __name__ == "__main__":
    # Example usage
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5]})
    processed_data = preprocess_data(data)
    print(processed_data)