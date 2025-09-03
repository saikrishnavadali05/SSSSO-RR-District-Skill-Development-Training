from flask import Flask, request

app = Flask(__name__)

@app.route('/bmi')
def bmi():
    return ''' 
        <div style="display:flex; justify-content:center; align-items:center; height:100vh; flex-direction:column;">
            <h2 style="color:blue;">BMI Calculator</h2>
            <form method="post" action="/result" style="font-size:18px; text-align:center; border:1px solid #ccc; padding:20px; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.2);">
                Weight (kg): <input type="text" name="weight" style="margin:5px;"><br><br>
                Height (m): <input type="text" name="height" style="margin:5px;"><br><br>
                <input type="submit" value="Calculate BMI" style="padding:5px 15px; font-size:16px;">
            </form>
        </div>
    '''

@app.route('/result', methods=['POST'])
def result():
    weight_input = request.form['weight']
    height_input = request.form['height']

    # Check for empty inputs
    if not weight_input or not height_input:
        return '''
            <div style="display:flex; justify-content:center; align-items:center; height:100vh; flex-direction:column;">
                <h2 style="color:red;">Both weight and height are required!</h2>
                <a href="/bmi" style="font-size:16px;">Back</a>
            </div>
        '''

    try:
        weight = float(weight_input)
        height = float(height_input)

        # Check for zero height
        if height == 0:
            return '''
                <div style="display:flex; justify-content:center; align-items:center; height:100vh; flex-direction:column;">
                    <h2 style="color:red;">Height cannot be zero!</h2>
                    <a href="/bmi" style="font-size:16px;">Back</a>
                </div>
            '''
    except ValueError:
        return '''
            <div style="display:flex; justify-content:center; align-items:center; height:100vh; flex-direction:column;">
                <h2 style="color:red;">Please enter valid numbers for weight and height!</h2>
                <a href="/bmi" style="font-size:16px;">Back</a>
            </div>
        '''

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 25:
        category = 'Normal weight'
    elif bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obese'

    return f'''
        <div style="display:flex; justify-content:center; align-items:center; height:100vh; flex-direction:column;">
            <h2>Your BMI is: {bmi}</h2>
            <h3>Category: {category}</h3>
            <a href="/bmi" style="font-size:16px;">Back</a>
        </div>
    '''

if __name__ == '__main__':
    app.run(debug=True)

