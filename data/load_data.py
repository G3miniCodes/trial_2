import generate_data
import logger

def load_dataset():
    logger.log_message("Loading dataset")
    data = generate_data.generate_dataset()
    return data
