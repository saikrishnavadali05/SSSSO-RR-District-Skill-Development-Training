#17.Remove all punctuation from a sentence using string.punctuation
import string
sen = "Sairam, Welcome! How are you? Aren't you a member of this samithi"
for p in string.punctuation:
    sen = sen.replace(p, '')
print(sen)