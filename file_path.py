import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def get_file_path(file_name: str) -> list[str]:
    try:
        with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as file:
            file_data = file.readlines()
            return file_data
    except:
        raise ValueError
