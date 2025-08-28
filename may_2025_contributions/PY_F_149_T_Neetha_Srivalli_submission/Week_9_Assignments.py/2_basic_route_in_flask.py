from flask import Flask   #Importing Flask class from flask module

app = Flask(__name__)     #Creating an instance of the Flask class

@app.route('/')     #Decorator to define the route for the home page
def home():
    return "Hello, Flask!"

if __name__ == '__main__':     #Check if the script runs directlt
    app.run(debug=True)

#Output:
# Flask app running on http://
