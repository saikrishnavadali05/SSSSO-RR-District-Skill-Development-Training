from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# ASCII representations for dice faces
dice_faces = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘",
    )
}

def roll_dice():
    return random.randint(1, 6)

# Template for the UI
template = """
<!DOCTYPE html>
<html>
<head>
    <title>🎲 Dice Roller</title>
    <style>
        body { font-family: monospace; background: #f0f0f0; text-align: center; padding: 40px; }
        .dice-face { font-size: 24px; line-height: 1.2; white-space: pre; display: inline-block; background: #fff; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
        button { margin-top: 20px; padding: 10px 20px; font-size: 16px; border: none; background-color: #007BFF; color: white; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <h1>🎲 Dice Roller Simulator</h1>
    {% if face %}
        <p>You rolled a <strong>{{ face }}</strong>!</p>
        <div class="dice-face">
            {{ dice_art|safe }}
        </div>
    {% endif %}
    <form method="post">
        <button type="submit">Roll Dice</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    face = None
    dice_art = ""
    if request.method == "POST":
        face = roll_dice()
        dice_art = "<br>".join(dice_faces[face])
    return render_template_string(template, face=face, dice_art=dice_art)

if __name__ == "__main__":
    app.run(debug=True)
