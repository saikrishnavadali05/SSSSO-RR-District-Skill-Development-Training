#19.String starts with a vowel and ends with a consonant.
word=input("Enter a word:")
if word[0].lower() in "aeiou" and word[-1].lower() not in "aeiou":
    print("Yes,string starts with a vowel and ends with a consonant.")
else:
    print("No,condition not met")