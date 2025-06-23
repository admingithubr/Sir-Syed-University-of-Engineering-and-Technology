import os, pickle

DATA_DIR = 'database'

def load_data(file):
    path = os.path.join(DATA_DIR, file)
    return pickle.load(open(path, 'rb')) if os.path.exists(path) else {}

def save_data(data, file):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, file), 'wb') as f:
        pickle.dump(data, f)
