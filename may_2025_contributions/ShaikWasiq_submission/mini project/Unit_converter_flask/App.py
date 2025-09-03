from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        conversion = request.form["conversion"]
        value = request.form["value"]
        try:
            value = float(value)
            if conversion == "km_miles":
                result = f"{value} km = {km_to_miles(value):.2f} miles"
            elif conversion == "miles_km":
                result = f"{value} miles = {miles_to_km(value):.2f} km"
            elif conversion == "kg_pounds":
                result = f"{value} kg = {kg_to_pounds(value):.2f} pounds"
            elif conversion == "pounds_kg":
                result = f"{value} pounds = {pounds_to_kg(value):.2f} kg"
            else:
                error = "Invalid conversion selected."
        except ValueError:
            error = "Please enter a valid number."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
