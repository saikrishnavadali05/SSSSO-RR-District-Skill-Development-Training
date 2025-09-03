from flask import Flask, render_template, jsonify, request, session
import random
from flask_session import Session

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

with open("words.txt", "r") as file:
    WORDS = [line.strip() for line in file if line.strip()]

def scramble(word):
    scrambled = list(word)
    while True:
        random.shuffle(scrambled)
        if "".join(scrambled) != word:
            break
    return "".join(scrambled)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_word")
def get_word():
    word = random.choice(WORDS)
    session["current_word"] = word
    return jsonify({"scrambled": scramble(word)})

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    guess = data.get("guess", "").strip().lower()
    correct_word = session.get("current_word", "")
    return jsonify({"correct": guess == correct_word, "word": correct_word})

if __name__ == "__main__":
    app.run(debug=True)
