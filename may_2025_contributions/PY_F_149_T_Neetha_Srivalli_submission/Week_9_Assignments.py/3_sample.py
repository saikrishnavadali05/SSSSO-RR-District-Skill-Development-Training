from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

text = "This is a sample sentence showing off the stop words filtration."
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stopwords.words('english')]

print("Filtered Text:", filtered)

#Output:
# Filtered Text: ['sample', 'sentence', 'showing', 'stop', 'words', 'filteration', '.']
