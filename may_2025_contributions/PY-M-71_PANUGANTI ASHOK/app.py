from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
HIGH_SCORE_FILE = "high_scores.txt"

THEMES = {
    "Classic Red": {"bg": "white", "trigger": "red"},
    "Cool Blue": {"bg": "#e0f7fa", "trigger": "#0077b6"},
    "Green Zen": {"bg": "#e8f5e9", "trigger": "#2e7d32"},
    "Dark Mode": {"bg": "#212121", "trigger": "#ff1744", "fg": "white"}
}

@app.route("/")
def home():
    return render_template("index.html", themes=THEMES)

@app.route("/theme", methods=["POST"])
def theme():
    selected = request.json["theme"]
    return jsonify(THEMES[selected])

@app.route("/record", methods=["POST"])
def record():
    reaction_time = float(request.json["time"])
    scores = load_scores()
    scores.append(reaction_time)
    scores.sort()
    scores = scores[:3]
    save_scores(scores)
    return jsonify(scores=scores)

def load_scores():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE) as f:
            return [float(x.strip()) for x in f.readlines()]
    return []

def save_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as f:
        for s in scores:
            f.write(f"{s:.3f}\n")

if __name__ == "__main__":
    app.run(debug=True)
