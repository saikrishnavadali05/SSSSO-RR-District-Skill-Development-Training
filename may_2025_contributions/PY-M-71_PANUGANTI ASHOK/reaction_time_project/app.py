from flask import Flask, render_template, request, jsonify
from score_logic import update_scores
from score_storage import load_scores, save_scores

app = Flask(__name__)
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
    scores = update_scores(reaction_time)
    save_scores(scores)
    return jsonify(scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
