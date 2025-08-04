from flask import Flask, render_template, request

app = Flask(__name__)

def convert_currency_static(amount, from_currency, to_currency):
    exchange_rates = {
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1.09,
        ('USD', 'INR'): 83.14,
        ('INR', 'USD'): 0.012,
    }

    key = (from_currency.upper(), to_currency.upper())
    if from_currency.upper() == to_currency.upper():
        return amount

    return amount * exchange_rates[key] if key in exchange_rates else None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None        

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency'].strip().upper()
            to_currency = request.form['to_currency'].strip().upper()

            result = convert_currency_static(amount, from_currency, to_currency)
            if result is None:
                error = "Exchange rate not found."
        except ValueError:
            error = "Invalid amount entered. Please enter a numeric value."
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)      
