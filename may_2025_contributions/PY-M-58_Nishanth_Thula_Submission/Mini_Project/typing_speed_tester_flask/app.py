from flask import Flask, render_template, request, redirect, url_for, session
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for session

TEXT_TO_TYPE = "GeeksforGeeks"

@app.route('/')
def index():
    session['start_time'] = time.time()  # save start time in session
    return render_template('index.html', text=TEXT_TO_TYPE)

@app.route('/result', methods=['POST'])
def result():
    end_time = time.time()
    start_time = session.get('start_time')
    if not start_time:
        return redirect(url_for('index'))

    user_input = request.form['typed_text']
    time_taken = end_time - start_time
    time_in_minutes = time_taken / 60

    word_count = len(TEXT_TO_TYPE.split())
    wpm = word_count / time_in_minutes

    # Calculate accuracy
    correct_chars = sum(
        1 for i, c in enumerate(user_input) if i < len(TEXT_TO_TYPE) and c == TEXT_TO_TYPE[i]
    )
    accuracy = (correct_chars / len(TEXT_TO_TYPE)) * 100

    return render_template(
        'result.html',
        time_taken=f"{time_taken:.2f}",
        wpm=f"{wpm:.2f}",
        accuracy=f"{accuracy:.2f}"
    )

if __name__ == '__main__':
    app.run(debug=True)
    
# This code is a Flask web application that serves as a typing speed tester.
# It measures the time taken to type a given text, calculates the typing speed in words per minute (WPM),
# and checks the accuracy of the typed text compared to the original text.