import string
text = input("Enter a sentence: ")
no_punct = "".join(char for char in text if char not in string.punctuation)
print(no_punct)