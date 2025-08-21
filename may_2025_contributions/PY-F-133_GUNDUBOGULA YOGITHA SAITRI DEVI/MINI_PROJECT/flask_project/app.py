from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion rates
conversion_rates = {
    '1': ('USD', 'INR', 83.4),
    '2': ('INR', 'USD', 0.012),
    '3': ('EUR', 'INR', 90.2),
    '4': ('INR', 'EUR', 0.011),
    '5': ('GBP', 'INR', 105.6),
    '6': ('INR', 'GBP', 0.0095)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        choice = request.form['conversion']
        amount = float(request.form['amount'])

        if choice in conversion_rates:
            from_curr, to_curr, rate = conversion_rates[choice]
            result = amount * rate
            result_msg = f"{amount} {from_curr} = {result:.2f} {to_curr}"
            return render_template('index.html', result=result_msg)
        else:
            return render_template('index.html', error="Invalid conversion selected.")

    except Exception as e:
        return render_template('index.html', error="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)