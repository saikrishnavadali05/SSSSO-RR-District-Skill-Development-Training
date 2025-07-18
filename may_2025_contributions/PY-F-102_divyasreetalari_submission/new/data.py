import json
import os

USER_FILE = "user.json"
SCORE_FILE = "score.json"

def load_json(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({}, f)
    with open(file, 'r') as f:
        return json.load(f)

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def get_users():
    return load_json(USER_FILE)

def save_users(data):
    save_json(USER_FILE, data)

def get_scores():
    return load_json(SCORE_FILE)

def save_scores(data):
    save_json(SCORE_FILE, data)
