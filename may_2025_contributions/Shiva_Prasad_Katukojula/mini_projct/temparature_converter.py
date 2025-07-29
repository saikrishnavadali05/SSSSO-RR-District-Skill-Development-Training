from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion Logic
def convert_temperature(temp_input, from_unit, to_unit):
    try:
        temp_input = float(temp_input)

        # Convert input to Celsius
        if from_unit == "Celsius":
            celsius = temp_input
        elif from_unit == "Fahrenheit":
            celsius = (temp_input - 32) * 5 / 9
        elif from_unit == "Kelvin":
            celsius = temp_input - 273.15
        elif from_unit == "Rankine":
            celsius = (temp_input - 491.67) * 5 / 9
        else:
            return "Invalid input unit"

        # Convert Celsius to target
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = celsius * 9 / 5 + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15
        elif to_unit == "Rankine":
            result = (celsius + 273.15) * 9 / 5
        else:
            return "Invalid target unit"

        return f"{round(result, 2)} °{to_unit[0]}"
    except ValueError:
        return "Invalid input. Please enter a number."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        temp_input = request.form.get("temp_input")
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")
        result = convert_temperature(temp_input, from_unit, to_unit)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
