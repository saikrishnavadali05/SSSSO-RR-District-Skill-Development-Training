def long_words(sentence):
    return [word for word in sentence.split() if len(word) > 4]

s = input("Enter a sentence: ")
print("Words with more than 4 letters:", long_words(s))