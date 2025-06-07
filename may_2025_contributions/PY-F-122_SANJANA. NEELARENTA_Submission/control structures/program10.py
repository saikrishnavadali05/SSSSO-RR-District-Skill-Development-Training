#Write a program to check if a character is a vowel or consonant using if-else.

ch = input("Enter a letter: ")

if ch in 'aeiouAEIOU':
    print(ch, "is a vowel.")
else:
    print(ch, "is a consonant.")
