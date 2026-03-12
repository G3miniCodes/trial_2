import datetime


def log_message(message):
    time = datetime.datetime.now()
    print(f"[{time}] {message}")
