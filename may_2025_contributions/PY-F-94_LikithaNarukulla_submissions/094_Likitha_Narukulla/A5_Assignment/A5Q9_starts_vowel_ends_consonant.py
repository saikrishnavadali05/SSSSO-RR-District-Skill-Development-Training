word = input("Enter a word: ").lower()
vowels = "aeiou"
if word[0] in vowels and word[-1] not in vowels:
    print("Starts with vowel and ends with consonant")
else:
    print("Condition not met")