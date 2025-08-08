#   from nltk.stem import WordNetLemmatizer   --Importing WordNetLemmatizer from nltk library
#   from nltk.corpus import wordnet   --Importing wordnet corpus for Lemmatization

#   nltk.download('wordnet')    --Download WordNet corpus
#   nltk.download('omw-1.4')     --Download Open Multilingual WordNet

#   lemmatizer = WordNetLemmatizer()   --Creating an instance of WordNetLemmatizer
#   words = ["playing", "played", "plays", "better", "children"]

#   lemmatized_words = [lemmatizer.lemmatize(w, pos='v') for w in words]
#   print("Lemmatized Words:", lemmatized_words)

#Output:
# Lemmatized Words: ['play', 'play', 'play', 'better', 'children']
