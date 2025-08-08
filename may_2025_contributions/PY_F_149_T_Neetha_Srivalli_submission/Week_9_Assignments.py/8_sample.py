sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

print("POS Tags:", pos_tags)

#Output:
# POS Tags: [("The/DT", "quick/JJ"), ("brown/JJ", "fox/NN"), ("jumps/VBZ", "over/IN"), ("the/DT", "lazy/JJ"), ("dog/NN", ".")]
