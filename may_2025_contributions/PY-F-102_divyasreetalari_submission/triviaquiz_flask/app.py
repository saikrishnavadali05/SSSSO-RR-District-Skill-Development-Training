from flask import Flask, render_template, jsonify
from quiz_api import get_questions
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Don't give full path

@app.route("/api/quiz")
def quiz_api():
    questions = get_questions()
    for q in questions:
        random.shuffle(q['options'])
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)
