# Main Flask app

from flask import Flask, render_template, jsonify
from quiz_api import get_questions
import os
import random

app = Flask(__name__)
cd=os.getcwd()
@app.route("/")
def home():
    # may_2025_contributions/PY-F-102_divyasreetalari_submission/triviaquiz_api_mini_project/template/index.html
    return render_template(cd+"may_2025_contributions/PY-F-102_divyasreetalari_submission/triviaquiz_api_mini_project/template/index.html")

@app.route("/api/quiz")
def quiz_api():
    questions = get_questions()
    for q in questions:
        random.shuffle(q['options'])
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)