import generate_data
import logger

def load_dataset():
    logger.log_message("Loading dataset")
    data = generate_data.generate_dataset()
    return data

def log_message(*args, **kwargs):
    raise NotImplementedError("Auto generated stub for 'log_message'")

def generate_dataset(*args, **kwargs):
    raise NotImplementedError("Auto generated stub for 'generate_dataset'")

if __name__ == "__main__":
    load_dataset()
