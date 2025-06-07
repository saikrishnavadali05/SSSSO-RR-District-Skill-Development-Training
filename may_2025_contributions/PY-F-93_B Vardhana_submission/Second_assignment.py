#1.Write a Python program to get the first and last character of a string.
def get_first_and_last_char(input_string):
    if not input_string:
        return "The string is empty."
    first_char = input_string[0]
    last_char = input_string[-1]
    return f"First character: '{first_char}', Last character: '{last_char}' "
user_input = input("Enter a string: ")
print(get_first_and_last_char(user_input))


#2.Check whether a string is palindrome or not
def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()  # Remove spaces and convert to lowercase for accurate comparison
    return cleaned_string == cleaned_string[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')


#3.Concatenate two strings using + operator and .format().
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Using + operator:", result)
res = "{} {}".format(str1, str2)
print("Using .format():", res)

#4.Use count() to find the number of occurrences of a character in a string.
user_input = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")
if not len(char_to_count) == 1:
    print("Please enter exactly one character to count.")
else:
    count = user_input.count(char_to_count)
    print(f"The character '{char_to_count}' appears {count} times in the string.")

#5.Compare two strings for equality, ignoring case sensitivity.
str1= input("Enter first string: ")
str2 = input("Enter second string: ")
if str1.casefold() == str2.casefold():
    print("Strings are equal (case-insensitive).")
else:
    print("Strings are not equal.")

#6.Split a string on a comma and print each element
user_input = input("Enter items separated by commas: ")
items = user_input.split(",")
for item in items:
    print(item.strip())  # strip() removes extra spaces

#7.Remove all punctuation from a sentence 
import string

sentence = input("Enter a sentence: ")
cleaned = "".join(char for char in sentence if char not in string.punctuation)
print("Without punctuation:", cleaned)

#8.Extract the domain from an email address using slicing and split()
email = input("Enter your email address: ")
if "@" in email:
    domain = email.split('@')[1]
    print("Domain:", domain)
else:
    print("Invalid email address: no '@' found.")


#9.Check if a string starts with a vowel and ends with a consonant.
text=input("enter string: ").lower()
lst="aeiou"
if text[0] in lst and text[-1] not in lst and text[-1].isalpha():
    print("The word starts with vowel and consonants. ")
else:
    print("not found")

#10.Write a function that takes a sentence and returns only the words with more than 4 letters.
def func(sentence):
    return [word for word in sentence.split() if len(word) > 4]
user_input = input("Enter a sentence: ")
result = func(user_input)
print("Words with more than 4 letters:", result)

#11.Write a program that uses the double quote escape sequence \" inside a string enclosed by double quotes.
print("She said, \"Python is fun!\" and smiled.")

#12.Demonstrate how to use the tab escape sequence \t to format output in columns.
print("Name\t\tAge\tCity")
print("Alice\t\t25\tNew York")
print("Bob\t\t\t30\tLondon")
print("Charlie\t\t22\tSydney")

#13.Write a Python string that spans multiple lines using newline escape sequences
multiline_string = "This is line one.\nThis is line two.\nThis is line three."
print(multiline_string)

#14.Write a program to replace all backslashes in a Windows file path string with double backslashes
file_path = input("Enter a Windows file path: ")
safe_path = file_path.replace("\\", "\\\\")
print("Modified path:", safe_path)

#15.Write a program that prints a string with a mix of quotes and escaped characters correctly.
print("She said, \"It's time to learn Python!\"\nLet's start with:\n\t1. Strings\n\t2. Escape characters\nPath: C:\\Python\\Basics")

#16.Write a program that prints a dialogue between two people using newline and tab escape sequences for formatting.
print("Alice: Hi Bob!\n\tHow are you today?\nBob: Hey Alice!\n\tI'm good, thanks for asking.\n\tWhat about you?\nAlice: I'm doing well too.\n\tAre you ready for the meeting?\nBob: Yes, absolutely.\n\tLet's get started.")

#17.Write a Python program that reads a string input from the user and replaces all newline escape sequences with a space.
user_input = input("Enter a string (use \\n for newlines): ")
modified_string = user_input.replace("\\n", " ")
print("Modified string:", modified_string)

#18.Explain how escape sequences affect the length of a string. Write code to demonstrate your explanation.
Escape sequences like \n, \t, \\, etc., count as one character in a string — even though they may appear as more when typed.
s = "Line1\nLine2\tTabbed\\Backslash\"Quote\'"
print("String output:")
print(s)
# Show the actual characters and length
print("\nRaw string representation:", repr(s))
print("Length of the string:", len(s))

#19.Explain the effect of the alarm escape sequence \a and write a program that uses it.
\a is the bell (alert/alarm) escape sequence.
When printed, it sends a signal to the system to play a beep sound.
It’s often used to alert the user when something needs attention.

username = input("Enter username: ")
password = input("Enter password: ")
if username != "admin" or password != "1234":
    print("\aInvalid login attempt!\a Please try again.")
else:
    print("Access granted!")

#20.Print a string with a carriage return \r and explain its effect.
"\r"" stands for carriage return.It moves the cursor back to the beginning of the same line.
It does not add a new line.Any characters after \r overwrite the existing line content.

print("Hello, World!\rHi")


#21.Write a Python program to check if a number is positive, negative, or zero using if statement.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#22.Write a program to print the multiplication table of a given number using a for loop.
num = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#23.Write a program to check if a character is a vowel or consonant using if-else.
char = input("Enter a single alphabet: ").lower()
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
else:
    print("Please enter a single alphabetic character.")

#24.Write a program to print all prime numbers between 1 and 100 using for loop and if conditions.
print("Prime numbers between 1 and 100 are:")
for num in range(2, 101): 
    is_prime = True        
    
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=' ')

#25.Write a program to print a pyramid pattern of stars using nested for loops.
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    # Print spaces
    for space in range(rows - i):
        print(" ", end="")
    # Print stars
    for star in range(2 * i - 1):
        print("*", end="")
    # Move to next line
    print()

#26.Write a program to generate Fibonacci series up to n terms using a while loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b  # Update values
    count += 1

#27.Write a program to print all Armstrong numbers between 100 and 999 using nested loops.
print("Armstrong numbers between 100 and 999 are:")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (units ** 3)
    if num == sum_of_cubes:
        print(num)

#28.Write a program to find the sum of even and odd numbers separately from a list of numbers.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sum_even = 0
sum_odd = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

#29.Write a program to merge two sorted lists into a single sorted list using loops.
list1 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
list2 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
merged_list = []
i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
while i < len(list1):
    merged_list.append(list1[i])
    i += 1
while j < len(list2):
    merged_list.append(list2[j])
    j += 1
print("Merged sorted list:", merged_list)

#30.Write a program to check whether a given year is a leap year or not using control structures.
year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
