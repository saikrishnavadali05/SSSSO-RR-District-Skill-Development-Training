"""
BMI Calculator Web Application using Flask
Author: Jayasimha Valam
Date: July 15, 2025
"""

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into health categories"""
    if bmi < 18.5:
        return "Underweight", "warning"
    elif bmi < 25:
        return "Normal weight", "success"
    elif bmi < 30:
        return "Overweight", "warning"
    else:
        return "Obese", "danger"

@app.route('/')
def index():
    """Home page with BMI calculator form"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle BMI calculation"""
    try:
        # Get form data
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        # Validate input
        if weight <= 0 or height <= 0:
            flash('Please enter positive values for weight and height.', 'error')
            return redirect(url_for('index'))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category, alert_type = classify_bmi(bmi)
        
        # Get health recommendation
        if category == "Underweight":
            recommendation = "Consider consulting a healthcare provider about healthy weight gain."
        elif category == "Normal weight":
            recommendation = "Great! Maintain your current healthy lifestyle."
        elif category == "Overweight":
            recommendation = "Consider a balanced diet and regular exercise."
        else:
            recommendation = "Consult a healthcare provider for personalized advice."
        
        return render_template('result.html', 
                             weight=weight, 
                             height=height, 
                             bmi=round(bmi, 2), 
                             category=category, 
                             alert_type=alert_type,
                             recommendation=recommendation)
        
    except ValueError:
        flash('Please enter valid numeric values.', 'error')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/about')
def about():
    """About page with BMI information"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
