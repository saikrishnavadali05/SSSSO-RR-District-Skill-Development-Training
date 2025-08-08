words = ["playing", "flies", "better", "feet"]

# Stemming
stemmed = [PorterStemmer().stem(w) for w in words]

# Lemmatization
lemmatized = [lemmatizer.lemmatize(w) for w in words]

print("Original:", words)
print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized)

#Output:
# Original: ['playing', 'flies', 'better', 'feet']
# Stemmed: ['play', 'fli', 'better', 'feet']
# Lemmatized: ['playing', 'flies', 'better', 'feet']