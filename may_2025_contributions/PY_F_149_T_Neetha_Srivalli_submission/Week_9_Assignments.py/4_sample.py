from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["playing", "played", "plays", "easily", "fairly"]

stemmed_words = [stemmer.stem(w) for w in words]
print("Stemmed Words:", stemmed_words)

#Output:
# Stemmed Words: ['play', 'play, 'play', 'easili', 'fairly']