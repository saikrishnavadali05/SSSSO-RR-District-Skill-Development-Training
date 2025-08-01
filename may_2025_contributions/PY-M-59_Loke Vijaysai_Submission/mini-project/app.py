from flask import Flask, render_template_string
from score_analysis import read_scores, analyze_scores

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Statistics</title>
</head>
<body>
    <h1>📊 Quiz Statistics</h1>
    <ul>
        <li>Total Scores: {{ data.count }}</li>
        <li>Average: {{ data.average }}</li>
        <li>Median: {{ data.median }}</li>
        <li>Min Score: {{ data.min }}</li>
        <li>Max Score: {{ data.max }}</li>
    </ul>
    <h2>Grade Distribution</h2>
    <ul>
        {% for grade, count in data.grades.items() %}
        <li>{{ grade }}: {{ count }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    scores = read_scores("scores.csv")
    result = analyze_scores(scores)
    return render_template_string(HTML_TEMPLATE, data=result)

if __name__ == "__main__":
    app.run(debug=True)
