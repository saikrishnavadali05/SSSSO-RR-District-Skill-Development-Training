import os

HIGH_SCORE_FILE = "high_scores.txt"

def load_scores():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE) as f:
            return [float(x.strip()) for x in f]
    return []

def save_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as f:
        for s in scores:
            f.write(f"{s:.3f}\n")
