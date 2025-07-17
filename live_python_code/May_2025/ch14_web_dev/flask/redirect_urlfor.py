from flask import redirect, url_for
from flask import render_template
from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Logged in as {username}"
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/api/data')
def api_data():
    return jsonify({"name": "Flask", "version": "2.x"})

@app.route('/template')
def template():
    return render_template('index.html', title="Welcome", message="Hello from Flask")

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)