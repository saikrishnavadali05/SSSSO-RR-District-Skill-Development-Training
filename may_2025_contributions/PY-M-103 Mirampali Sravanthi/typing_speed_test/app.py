from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language.",
    "Typing speed is measured in words per minute.",
    "Flask makes web development easy and fun.",
    "Artificial Intelligence is transforming the world."
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original = request.form["original"]
        typed = request.form["typed"]
        start_time = float(request.form["start_time"])
        end_time = float(request.form["end_time"])

        elapsed_time = end_time - start_time
        words_typed = len(typed.split())
        wpm = round(words_typed / (elapsed_time / 60)) if elapsed_time > 0 else 0

        accuracy = calculate_accuracy(original, typed)

        return render_template("index.html", original=original, result=True, wpm=wpm, accuracy=accuracy)

    sentence = random.choice(sentences)
    return render_template("index.html", original=sentence, result=False)

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    return round((correct / len(original_words)) * 100) if original_words else 0

if __name__ == "__main__":
    app.run(debug=True)
