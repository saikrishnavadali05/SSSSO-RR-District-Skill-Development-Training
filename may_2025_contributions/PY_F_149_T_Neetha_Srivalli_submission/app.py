from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = ''
        session['game_over'] = False

    if request.method == 'POST' and not session.get('game_over'):
        guess = int(request.form['guess'])
        session['attempts'] += 1
        target = session['number']

        if guess == target:
            session['message'] = f"🎉 Correct! You guessed it in {session['attempts']} attempts."
            session['game_over'] = True
        elif abs(guess - target) == 1:
            session['message'] = "🔥 Very close! Try again."
        elif guess < target:
            session['message'] = "Too low! Try again."
        else:
            session['message'] = "Too high! Try again."

    return render_template("index.html",
                           message=session.get('message', ''),
                           attempts=session.get('attempts', 0),
                           game_over=session.get('game_over', False))

@app.route('/restart')
def restart():
    session.pop('number', None)
    session.pop('attempts', None)
    session.pop('message', None)
    session.pop('game_over', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

