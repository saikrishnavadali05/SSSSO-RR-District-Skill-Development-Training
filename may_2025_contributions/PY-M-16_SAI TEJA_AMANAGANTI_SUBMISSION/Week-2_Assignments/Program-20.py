#20.A function that takes a sentence and returns only the words with more than 4 letters
def long_words(sentence):
    return [word for word in sentence.split() if len(word) > 4]

print(long_words(input("Enter a sentence:")))