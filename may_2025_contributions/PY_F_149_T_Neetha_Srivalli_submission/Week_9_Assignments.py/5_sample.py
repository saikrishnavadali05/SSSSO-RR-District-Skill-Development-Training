from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
words = ["playing", "played", "plays", "better", "children"]

lemmatized_words = [lemmatizer.lemmatize(w, pos='v') for w in words]
print("Lemmatized Words:", lemmatized_words)

#Output:
# Lemmatized Words: ['play', 'play', 'play', 'better', 'children']
