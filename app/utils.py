import secrets
import time


def generate_filename(extension):
    current_time = str(int(time.time()))
    random_string = secrets.token_hex(8)
    filename = current_time + "_" + random_string + extension
    return filename
