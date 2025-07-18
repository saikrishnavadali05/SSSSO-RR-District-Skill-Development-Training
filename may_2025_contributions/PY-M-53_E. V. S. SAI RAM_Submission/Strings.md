```python
"""1. Write a Python program to get the first and last character of a string."""

str1 = input("enter a string : ")
print(f" first character of string {str1} is {str1[0]} and last character is {str1[-1]}")
```

    enter a string :  python
    

     first character of string python is p and last character is n
    


```python
"""2. Check whether a string is palindrome or not (e.g., "madam")."""
str2 = input("enter a string : ")

if str2 == str2[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")    

```

    enter a string :  madam
    

    String is a palindrome
    


```python
"""3. Use len() to find the length of any input string."""
str3 = input("enter a string : ")
print(f" length of string {str3} is {len(str3)}")
```

    enter a string :  hello
    

     length of string hello is 5
    


```python
"""4. Convert a given string to uppercase and lowercase using string methods"""
str4 = input("enter a string : ")
print(f" UpperCase of string {str4} is {str4.upper()}")
```

    enter a string :  sairam
    

     UpperCase of string sairam is SAIRAM
    


```python
""" 5. Concatenate two strings using + operator and .format() """
str5a = input("enter a string : ")
str5b = input("enter a string : ")
final = str5a+str5b
print("concatenated string is {:>20}".format(final))
```

    enter a string :  hello
    enter a string :  hi
    

    concatenated string is              hellohi
    


```python
""" 6.Print each character in a string using indexing and a loop """
str6 = input("enter a string : ")
for i in range(len(str6)):
    print(f" index {i} element is {str6[i]}")
```

    enter a string :  python
    

     index 0 element is p
     index 1 element is y
     index 2 element is t
     index 3 element is h
     index 4 element is o
     index 5 element is n
    


```python
""" 7.Slice a string to get every second character from index 1 to 10 """
str7 = input("enter a string : ")

for i in range(0, len(str7), 2):
    if i <11:
        print(f" index {i} element is {str7[i]}")    
```

    enter a string :  sairamsir
    

     index 0 element is s
     index 2 element is i
     index 4 element is a
     index 6 element is s
     index 8 element is r
    


```python
"""8. Use count() to find the number of occurrences of a character in a string."""
str8 = input("enter a string : ")

char = input("enter a char : ") 

print(f" in string {str8} occurances of {char} is {str8.count(char)} times")
```

    enter a string :  sairam
    enter a char :  a
    

     in string sairam occurances of a is 2 times
    


```python
"""9. Check if a substring is present in a given string using in."""
str9 = input("enter a string : ")
str9sub =  input("enter a sub string : ")
print(str9sub in str9)
```

    enter a string :  sairam help needed
    enter a sub string :  help
    

    True
    


```python
"""10. Take a user's name as input and print a greeting using .format()"""
str10 = input("enter a name : ")
print("{:<20}  {:>20}".format("greetings" , str10))
```

    enter a name :  sairam
    

    greetings                           sairam
    


```python
"""11. Write a function to reverse a string using slicing"""

def reverse_string(s):
    return s[::-1]

str11 = input("enter a string : ")
reversed_string = reverse_string(str11)
print(f"reverse of {str10} is {reversed_string}")
```

    enter a string :  sairam
    

    reverse of sairam is marias
    


```python
"""12. Check whether a string contains only digits using built-in functions"""

str12 = input("enter a string : ")

if str12.isdigit():
    print("The string contains only digits.")
else:
    print("The string contains non-digit characters aswell.")

```

    enter a string :  123456
    

    The string contains only digits.
    


```python
"""13. Replace all spaces in a string with dashes"""
str13 = input("enter a string : ")
new_str13 = str13.replace(" ", "-")
print(f"updated string is {new_str13}")
```

    enter a string :  sai ram
    

    updated string is sai-ram
    


```python
"""14. Capitalize the first letter of every word in a sentence using title()"""
str14 = input("enter a string : ")
print(f"capitalized string is {str14.title()}")

```

    enter a string :  sairam how are you
    

    capitalized string is Sairam How Are You
    


```python
"""15. Compare two strings for equality, ignoring case sensitivity"""
str15a = input("enter a string : ")
str15b = input("enter a string : ")

if str15a.lower() == str15b.lower():
    print("both strings are same")
else:
    print("both strings are different")
```

    enter a string :  hello
    enter a string :  Hello
    

    both strings are same
    


```python
"""16. Split a string on a comma and print each element"""
str16 = input("enter a string : ")

print(str16.split(','))
```

    enter a string :  hello,sairam,hi
    

    ['hello', 'sairam', 'hi']
    


```python
"""17. Remove all punctuation from a sentence (hint: use string.punctuation)"""
import string # module to be imported to use its content
str17 = input("enter a string : ")
str17_copy = str17

for i in range(0,len(str17)):
    if str17[i] in string.punctuation :
        str17_copy = str17_copy.replace(str17[i], '')

print(f"after removing punctuation : {str17_copy}")
```

    enter a string :  hello! "I know"
    

    after removing punctuation : hello I know
    


```python
"""18. Extract the domain from an email address using slicing and split()"""
str18 = input("enter a emailid : ")
print(f"domain is {str18.split('@')[1]}")
```

    enter a emailid :  sairam@gmail.com
    

    domain is gmail.com
    


```python
"""19. Check if a string starts with a vowel and ends with a consonant"""
str19 = input("enter a string : ")
vowels = ['a','e','i','o','u']
if str19[0] in vowels and str19[-1] not in vowels:
    print("string starts with vowel and ends with consonent")
else:
    print('"string starts with vowel and ends with consonent" condition not met')
```

    enter a string :  apples
    

    string starts with vowel and ends with consonent
    


```python
"""20. Write a function that takes a sentence and returns only the words with more than 4 letters"""
str20 = input("enter a sentence : ")
str20_words = str20.split(' ')

for i in str20_words:
    if len(i) > 4:
        print(i)
```

    enter a sentence :  help sairam
    

    sairam
    


```python
"""21. Create a custom string formatting function using format() and positional arguments"""

def custom_format(string, *args):
    """
    Custom formatting function that inserts positional arguments into the format string.
    """
    return string.format(*args)


string = custom_format("hello {0:<10} My name is {1:>10}", "brother", "sairam")
print(string)
```

    hello brother    My name is     sairam
    


```python
"""22. Write a program to find the longest word in a sentence"""
str22 = input("enter a sentence : ")
str22_words = str22.split(' ')

longest_word =  str22_words[0]

for i in str22_words:
    if len(i) > len(longest_word):
        longest_word = i
print(f"longest word in sentence is : {longest_word}")
```

    enter a sentence :  hello sairam im learning python
    

    longest word in sentence is : learning
    


```python
"""23. Count the frequency of each character in a string and display as a dictionary"""
str23 = input("enter a string : ")
dict_string = {}
for i in str23:
    dict_string[i]=str23.count(i)

print(dict_string)
```

    enter a string :  hello sairam
    

    {'h': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 's': 1, 'a': 2, 'i': 1, 'r': 1, 'm': 1}
    


```python
"""24. Implement a Caesar cipher (basic encryption by shifting characters)"""
def caesar_cipher(string, shift):
    str_copy = ''
    for i in string:
        str_copy = str_copy + (chr(ord(i) + shift))
    return str_copy

str24 = input("enter a string : ")

print(f"encrypted text : {caesar_cipher(str24,2)}")
```

    enter a string :  apple
    

    encrypted text : crrng
    


```python
"""25. Write a function to normalize whitespace in a string (multiple spaces to one)"""

def normalize_string(string):
    new_str = ''
    for i in str25.split():
        new_str = new_str + " " + i
    return new_str


str25 = input("enter a sentence : ")

print(f"normalized value : {normalize_string(str25)}" )

```

    enter a sentence :  hello   how    are you
    

    normalized value :  hello how are you
    


```python
"""26. Generate a unique hash from a string using hash() and explain its use case"""
""" hash() is a built in fuction in python that returns a hashed integer value of a given input"""
str26 = input("enter a string : ")

print(f" hash value of {str26} : {hash(str26)}")

```

    enter a string :  sai
    

     hash value of sai : 6311203760996430594
    


```python
"""27.Find all unique substrings of length k in a given string"""
str27 = input("enter a string : ")
char_len = int(input('enter lenth of sub string : '))

unique = []
for i in range(len(str27) - char_len  + 1):
    substring = str27[i:i+char_len]
    if substring not in unique:
        unique.append(substring)
print(unique)
```

    enter a string :  sairam sai brother
    enter lenth of sub string :  3
    

    ['sai', 'air', 'ira', 'ram', 'am ', 'm s', ' sa', 'ai ', 'i b', ' br', 'bro', 'rot', 'oth', 'the', 'her']
    


```python
"""28.Check if one string is a rotation of another (e.g., "abc" and "cab")"""
str28a = input("enter a string : ")
str28b = input("enter a string : ")
rotation = ''
for i in str28b:
    if i in str28a:
        rotation += i
if len(str28a) == len(rotation):
    print("second string is rotation of first string")
else:
    print("second string is not rotation of first string")    


```

    enter a string :  sairam
    enter a string :  ramsai
    

    second string is rotation of first string
    


```python
"""29.Implement a string compression algorithm (e.g., "aaabbb" → "a3b3")"""
str29 = input("enter a string : ")
counter = 0
prev = str29[0]
comp_string = ''

for i in range(len(str29)):
    
    if str29[i] == prev:
        counter += 1
    else:
        comp_string = comp_string + prev + str(counter)
        prev = str29[i]
        counter = 1
    if i==len(str29)-1:
        comp_string = comp_string + prev + str(counter)


print(f"compressed string : {comp_string}")
```

    enter a string :  abbcccdddde
    

    compressed string : a1b2c3d4e1
    


```python
"""30.Write a decorator that logs the input and output of any string processing function"""

def log_io(func):
    def wrapper(*args):
        print(f"Function: {func.__name__}")
        print("Input:", *args)
        result = func(*args)
        print("Output:", result)
    return wrapper


@log_io
def reverse_string(s):
    return s[::-1]

@log_io
def caesar_cipher(string, shift):
    str_copy = ''
    for i in string:
        str_copy = str_copy + (chr(ord(i) + shift))
    return str_copy


reverse_string("hello")

caesar_cipher('sai',3)
```

    Function: reverse_string
    Input: hello
    Output: olleh
    Function: caesar_cipher
    Input: sai 3
    Output: vdl
    


```python

```
