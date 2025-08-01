import os
import json

# In-memory databases
users_db = {}
scores_db = {}
quiz_db = []

# Determine the current directory of this file
BASE_DIR = os.path.dirname(__file__)

# Full paths to your JSON files
users_path = os.path.join(BASE_DIR, "users.json")
scores_path = os.path.join(BASE_DIR, "scores.json")

# Load users from users.json if it exists
if os.path.exists(users_path):
    try:
        with open(users_path, "r") as f:
            users_db.update(json.load(f))
    except json.JSONDecodeError:
        print(" users.json is corrupted. Starting with empty users_db.")

# Load scores from scores.json if it exists
if os.path.exists(scores_path):
    try:
        with open(scores_path, "r") as f:
            scores_db.update(json.load(f))
    except json.JSONDecodeError:
        print("⚠️ scores.json is corrupted. Starting with empty scores_db.")

# Function to save users to users.json
def save_users():
    with open(users_path, "w") as f:
        json.dump(users_db, f, indent=4)

# Function to save scores to scores.json
def save_scores():
    with open(scores_path, "w") as f:
        json.dump(scores_db, f, indent=4)
