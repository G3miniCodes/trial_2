import utils.helpers


def create_features(data):
    data['x1_sq'] = square(data['x1'])
    data['x2_sq'] = square(data['x2'])
    return data
