from nltk import pos_tag, ne_chunk

nltk.download('maxent_ne_chunker')
nltk.download('words')

sentence = "Barack Obama was the 44th President of the United States."
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)
tree = ne_chunk(tags)

print(tree)

#Output:
# (S)
#   (PERSON Barack/NNP obama/NNP)
#   was/VBD
#   The/DT
#   44th/JJ
#   President/NNP
#   of/IN
#   the/DT
#   United/NNP
#   States/NNPS
#   ./.