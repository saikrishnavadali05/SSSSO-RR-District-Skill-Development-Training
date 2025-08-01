from flask import Flask, render_template, request, jsonify
import random
from collections import Counter # Import Counter for counting occurrences

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main index.html page for the Coin Toss Simulator.
    """
    return render_template('index.html')

@app.route('/simulate_toss', methods=['POST'])
def simulate_toss():
    """
    Handles the coin toss simulation logic on the backend.
    Receives num_tosses and heads_prob from the frontend, performs the simulation,
    and returns the results as JSON.
    """
    data = request.get_json()
    num_tosses = data.get('num_tosses', 10)
    heads_prob = data.get('heads_prob', 0.5)

    # Input validation
    if not isinstance(num_tosses, int) or num_tosses <= 0:
        return jsonify({"error": "Invalid number of tosses. Must be a positive integer."}), 400
    if not isinstance(heads_prob, (float, int)) or not (0 <= heads_prob <= 1):
        return jsonify({"error": "Invalid heads probability. Must be between 0 and 1."}), 400

    results = []
    # Loop to simulate multiple coin flips
    for _ in range(num_tosses):
        # Random selection from a list (Heads or Tails) based on probability
        toss = random.choices(['Heads', 'Tails'], weights=[heads_prob, 1 - heads_prob])[0]
        results.append(toss)

    # Counting occurrences using collections.Counter
    counts = Counter(results)
    heads = counts['Heads']
    tails = counts['Tails']

    # Calculate percentages
    heads_percent = (heads / num_tosses) * 100 if num_tosses > 0 else 0
    tails_percent = (tails / num_tosses) * 100 if num_tosses > 0 else 0

    return jsonify({
        "heads": heads,
        "tails": tails,
        "heads_percent": round(heads_percent, 2),
        "tails_percent": round(tails_percent, 2),
        "toss_results": results # Sending individual results for display (optional, can be large)
    })

if __name__ == '__main__':
    # Run the Flask application.
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    app.run(debug=True)
