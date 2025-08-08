import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

text = "Python is great. It is used in machine learning and data science."
sentences = sent_tokenize(text)
words = word_tokenize(text)

print("Sentences:", sentences)
print("Words:", words)
#Output:
# Sentences: ['Python is great.', 'It is used in machine learning and data science.']
# Words: ['Python', 'is', 'great', '.', 'It', 'is', 'used', 'in', 'machine', 'learning', 'and', 'data', 'science', '.']