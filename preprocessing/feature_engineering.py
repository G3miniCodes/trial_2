import utils.helpers as helpers

def create_features(data):
    data['x1_sq'] = helpers.square(data['x1'])
    data['x2_sq'] = helpers.square(data['x2'])
    return data

def square(x):
    raise NotImplementedError("Auto generated stub for 'square'")
