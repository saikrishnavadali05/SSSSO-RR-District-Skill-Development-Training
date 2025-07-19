#Basic------------------------------
#1.Get the first and last character of a string
sentence=input("Enter a string:")
if sentence:
    print("First character",sentence[0]," Last character",sentence[-1])
else:
    print("String not given")

#2. string is palindrome or not 
pal=input("Enter a string:")
if pal==pal[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#3.length of any input string
l=input("Enter a string:")
print("The length of the string is",len(l))
    
#4.Convert a given string to uppercase and lowercase
string=input("Enter a string:")
if string:
    print("Converted string to Uppercase:",string.upper())
    print("Converted string to Lowercase:",string.lower())
else:
    print("Please enter valid string")

#5.Concatenate two strings using + operator and .format()
s1=input("Enter a string 1:")
s2=input("Enter a string 2:")
if s1 and s2:
    print("Concatenated two strings using + operator",s1+" "+s2)
    print("Concatenated two strings using .format()","{} {}".format(s1,s2))
else:
    print("Please enter valid strings")

#6.Print each character in a string using indexing and a loop
stn = input("Enter a string: ")
for i in range(len(stn)):
    print(stn[i])

#7.Slice a string to get every second character from index 1 to 10.
s = input("Enter a string: ")
if s:
    print("Every second character of the string:",s[1:10:2])
else:
    print("Please enter valid string")

#8.Count the number of occurrences of a character in a string
sw = input("Enter a string: ")
character= input("Enter the character whose count is required: ")
if sw:
    if character:
        print("Count of occurences of character in the string:",sw.count(character))
    else:
        print("Character not given")
else:
    print("String not given")

#9.substring is present in a given string
words = input("Enter the main string: ")
substr = input("Enter the substring to search for: ")
if substr in words:
    print("Substring is present in the main string")
else:
    print("Substring is not present in the main string")

#10.Greet user using .format().
Name = input("Enter your Name: ")
if Name:
    print( "Sairam, {}! How are you?".format(Name))
else:
    print("Please enter valid Name")

#Intermediate----------------------
#11.Reverse a string using slicing
def reversestring(st):
    return st[::-1]

print("Reversed string:",reversestring(input("Enter a string: ")))

#12.String contains only digits using built-in functions
sg = input("Enter a string: ")
if sg.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

#13.Replace all spaces in a string with dashes
sg = input("Enter a string: ")
if sg:
    print("Space replaced with dashes string:", sg.replace(" ", "-"))
else:
    print("Please enter a valid string")

#14.Capitalize the first letter of every word in a sentence using title()
sentence = input("Enter a sentence: ")
print("Capitalize the first letter in sentence:", sentence.title())

#15.Compare two strings for equality, ignoring case sensitivity
str1=input("Enter a string 1:")
str2=input("Enter a string 2:")
if str1.lower()==str2.lower():
    print("The two strings are equal")
else:
    print("The two strings are not equal")

#16.Split a string on a comma and print each element
text = input("Enter a string with commas : ")
elements = text.split(',')
for element in elements:
    print(element.strip())

#17.Remove all punctuation from a sentence using string.punctuation
import string
sen = "Sairam, Welcome! How are you? Aren't you a member of this samithi?"
for p in string.punctuation:
    sen = sen.replace(p, '')
print(sen)

#18.Extract the domain from an email address using slicing and split()
email=input("Enter email id : ")
if '@' in email and email.count('@') == 1 and email.index('@') != 0 and email.index('@') != len(email) - 1:
    domain = email.split('@')[-1]  
    print("Domain:", domain)
else:
    print("Invalid email address")

#19.String starts with a vowel and ends with a consonant.
word=input("Enter a word:").strip()
if not word:
    print("No input given")
elif word[0].lower() in "aeiou" and word[-1].lower() not in "aeiou":
    print("Yes,string starts with a vowel and ends with a consonant.")
else:
    print("No,condition not met")

#20.A function that takes a sentence and returns only the words with more than 4 letters
def long_words(sentence):
    return [word for word in sentence.split() if len(word) > 4]

print(long_words(input("Enter a sentence:")))

#Advanced---------------------
#21. A custom string formatting function using format() and positional arguments
def custom_string(name, age):
    return "Name: {}, Age: {}".format(name, age)

print(custom_string("Swami",100))

#22.Find the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word(input("Enter a sentence with long words:")))

#23.Count the frequency of each character in a string and display as a dictionary
def character_freq(f):
    freq = {}
    for c in f:
        freq[c] = freq.get(c, 0) + 1
    return freq

print(character_freq(input("Enter a string:")))

#24.Implement a Caesar cipher (basic encryption by shifting characters)
def caesar_cipher(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

print(caesar_cipher("def DEF", 2))

#25.a function to normalize whitespace in a string (multiple spaces to one)
def normalize_whitespace(NW):
    return ' '.join(NW.split())

print(normalize_whitespace(input("Enter a sentenence with spaces:")))

#26.Generate a unique hash from a string using hash() and explain its use case
si=input("Enter a string:")
print(hash(si))

#27.Find all unique substrings of length k in a given string
def unique_substrings(s, k):
    return set(s[i:i+k] for i in range(len(s)-k+1))

print(unique_substrings(input("Enter a string with more than two chracters:"),2))

#28.one string is a rotation of another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

print(is_rotation(input("Enter a string 1:"),input("Enter a string 2:") ))

#29.Implement a string compression algorithm
def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + (str(count) if count > 1 else '')
            count = 1
    return result

print(compress_string(input("Enter a string with repeated characters:")))

#30.A decorator that logs the input and output of any string processing function
def log_io(f):
    def text(x):
        print("Input string:", x)
        y = f(x)
        print("Output string:", y)
        return y
    return text

@log_io
def uppercase_fun(s):
    return s.upper()

uppercase_fun(input("Enter a string:"))