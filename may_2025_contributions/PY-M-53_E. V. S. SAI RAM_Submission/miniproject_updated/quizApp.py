from flask import Flask, render_template, request, redirect
import json
import os
import random

# Set up Flask with explicit template folder path
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
QUIZ_FILE = os.path.join(BASE_DIR, "quiz.json")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Load questions from JSON file
with open(QUIZ_FILE, "r") as f:
    QUESTIONS = json.load(f)

# Store quiz state in memory (for one user at a time)
quiz_state = {
    "current": 0,
    "score": 0,
    "questions": []
}

@app.route("/")
def home():
    quiz_state["current"] = 0
    quiz_state["score"] = 0

    # Make a copy of questions and shuffle them
    quiz_state["questions"] = QUESTIONS[:]
    random.shuffle(quiz_state["questions"])

    return redirect("/question")

@app.route("/question", methods=["GET", "POST"])
def question():
    if request.method == "POST":
        selected = request.form.get("answer")
        current_q = quiz_state["questions"][quiz_state["current"]]
        correct_answer = current_q["options"][current_q["answer"] - 1]

        # Check answer and update score
        if selected == correct_answer:
            quiz_state["score"] += 1

        quiz_state["current"] += 1  # Move to next question

    # If no more questions, go to result page
    if quiz_state["current"] >= len(quiz_state["questions"]):
        return redirect("/result")

    # Show current question
    q = quiz_state["questions"][quiz_state["current"]]
    return render_template("question.html", question=q["question"], options=q["options"], countdown=10)

@app.route("/result")
def result():
    return render_template("result.html", score=quiz_state["score"], total=len(QUESTIONS))

if __name__ == "__main__":
    app.run(debug=True)
