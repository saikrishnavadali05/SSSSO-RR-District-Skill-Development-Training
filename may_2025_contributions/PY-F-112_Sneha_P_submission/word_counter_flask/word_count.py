from flask import Flask, request, render_template
import string
from collections import Counter

app = Flask(__name__)

def clean_text(text):
    # Remove punctuation and lowercase
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def count_words(text):
    # Splits the text into a list of words and returns a Counter object (dictionary)
    cleaned = clean_text(text)
    words = cleaned.split()
    return Counter(words)

@app.route('/', methods=['GET', 'POST'])
def index():
    wordcounts = None
    error = None
    input_text = ''
    if request.method == 'POST':
        # Check if file uploaded
        uploaded_file = request.files.get('file')
        if uploaded_file and uploaded_file.filename != '':
            if uploaded_file.filename.endswith('.txt'): #check uploaded file ends with.txt
                input_text = uploaded_file.read().decode('utf-8') #Reads the file
            else:
                error = "Only .txt files allowed!"
        else:
            # Or use textarea input
            input_text = request.form.get('textinput', '').strip()

        if input_text and not error:
            wordcounts = count_words(input_text)
        elif not error:
            error = "Please upload a file or enter text."

    return render_template('wordcount.html', wordcounts=wordcounts, error=error, text=input_text)

if __name__ == '__main__':
    app.run(debug=True)