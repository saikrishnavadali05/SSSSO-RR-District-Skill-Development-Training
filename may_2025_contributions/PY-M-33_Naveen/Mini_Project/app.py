from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)

@app.route('/')
def index():
    cards = models.get_all_cards()
    return render_template('index.html', cards=cards)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        models.add_card(request.form['term'], request.form['definition'])
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)