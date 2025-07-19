from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main index.html page for the Coin Toss Simulator.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application.
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    app.run(debug=True)

