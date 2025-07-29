from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def is_palindrome(text):
  cleaned = ''.join(char.lower() for char in text if char.isalnum())
  return cleaned == cleaned[::-1]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/check', methods = ['POST'])
def check_palindrome():
  data = request.json
  text = data.get('text', '') if data else ''
  result = is_palindrome(text)
  return jsonify({'result' : 'Palindrome' if result else 'Not a Palindrome'})

if __name__ == '__main__':
    app.run(debug=True)