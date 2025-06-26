```python
""" 1.Write a Python program to print a string that includes a newline escape sequence \n."""

str1 = input("enter a name : ")
print(f" Hello \n {str1}")
```

    enter a name :  sairam
    

     Hello 
     sairam
    


```python
"""2.Demonstrate how to use the tab escape sequence \t to format output in columns"""
str2a = input("enter a name : ")
str2b = input("enter age : ")
str2c = input("enter gender : ")
print(f" Details entered:\n{str2a}\t{str2b}\t{str2c}")
```

    enter a name :  sairam
    enter age :  29
    enter gender :  M
    

     Details entered:
    sairam	29	M
    


```python
"""3.Show an example of printing a backslash \\ in a string """

str3a = input("enter first preference color : ")
str3b = input("enter second preference color : ")

print(f" preference of color {str3a} \\ {str3b}")


```

    enter first preference color :  red
    enter second preference color :  green
    

     preference of color red \ green
    


```python
"""4.Write a program that uses the single quote escape sequence \' inside a string enclosed by single quotes """
str4 = input("enter a name : ")
print(f' Hello \'{str4}\' ')
```

    enter a name :  sairam
    

     Hello 'sairam' 
    


```python
"""5.Write a program that uses the double quote escape sequence \" inside a string enclosed by double quotes """
str5 = input("enter a name : ")
print(f" Hello \"{str5}\" ")
```

    enter a name :  sairam
    

     Hello "sairam" 
    


```python
"""6.Print a string with a carriage return \r and explain its effect"""
str6 = input("enter a string : ")
print(f"{str6}\rLast")

"""overrides initial characters of string with new string"""
```

    enter a string :  sairam
    

    Lastam
    




    'overrides initial characters of string with new string'




```python
"""7.Write a program demonstrating the backspace escape sequence \b by deleting characters from a printed string."""
str7 = input("enter a string : ")
print(f"{str7}\b\b123")
```

    enter a string :  sairam
    

    sair123
    


```python
"""8.Show how to print a string that contains both single and double quotes using escape sequences."""
str8a = input("enter a name : ")
str8b = input("enter age : ")

print(f" Name \"{str8a}\"\tage\'{str2b}\'")
```

    enter a name :  sairam
    enter age :  29
    

     Name "sairam"	age'29'
    


```python
"""9.Explain the effect of the alarm escape sequence \a and write a program that uses it."""

print("Show starting...")
for i in range(10, 0, -1):
    print(i)

print("\aShow Time!")

"""If your terminal or console supports it and system sound is enabled, you’ll hear a beep.
Otherwise, it might just silently display the message without the beep."""
```

    Show starting...
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Show Time!
    




    'If your terminal or console supports it and system sound is enabled, you’ll hear a beep.\nOtherwise, it might just silently display the message without the beep.'




```python
"""10.Write a Python string that spans multiple lines using newline escape sequences."""
str10a = input("enter a name : ")
str10b = input("enter age : ")
print(f"Name: {str10a}\nAge: {str10b}")
```

    enter a name :  sairam
    enter age :  29
    

    Name: sairam
    Age: 29
    


```python
"""11.Create a program that prints a formatted table using tabs (\t) and newlines (\n)"""

table = "Name\t|\tAge\n"
length = len(table)

table = table + '-'*length*2 + '\n'

# Add 1st row to the table
table += "SaiRam\t|\t29\n"

table = table + '-'*length*2 + '\n'

# Add 2nd row to the table
table += "Krishna\t|\t25\n"

table = table + '-'*length*2 + '\n'


# Print the table
print(table)
```

    Name	|	Age
    ----------------------
    SaiRam	|	29
    ----------------------
    Krishna	|	25
    ----------------------
    
    


```python
"""12.Write a program to replace all backslashes in a Windows file path string with double backslashes"""

str12 = input('enter path : ')
str12_new = str12.replace('\\','\\\\')

print(f" updated path : {str12_new}")
```

    enter path :  c:\sairam\folder
    

     updated path : c:\\sairam\\folder
    


```python
"""13.Explain and demonstrate how carriage return \r can be used to overwrite output on the same line"""

str13a = input("enter a string : ")
str13b = input("enter a string : ")

print(f"{str13a}\r{str13b}")
```

    enter a string :  sai
    enter a string :  ram
    

    ram
    


```python
"""14.Write a program that prints a string with a mix of quotes and escaped characters correctly"""

str14 = '"Hello"\n\'SaiRam\'\n"good morning"'
print(str14)

```

    "Hello"
    'SaiRam'
    "good morning"
    


```python
"""15.Demonstrate the difference between printing a string with and without escape sequences using raw strings (prefix r)"""

normal_string = "SaiRam\nHello\t!"

# Raw string: escape sequences are NOT processed
raw_string = r"Hello\nSairam\t!"

print("Normal string:")
print(normal_string)

print("\nRaw string:")
print(raw_string)
```

    Normal string:
    SaiRam
    Hello	!
    
    Raw string:
    Hello\nSairam\t!
    


```python
"""16.Write a program that prints a progress bar animation using carriage return \r"""
import time
for i in range(10 + 1):
    percent = int((i / 10) * 100)
    bar_length = 10  # length of the progress bar
    filled_length = int(bar_length * i // 10)
    bar = '|' * filled_length + '-' * (bar_length - filled_length)        
    # \r moves cursor to start
    print(f'\rProgress: {bar} {percent}%',end='')
    time.sleep(1)
    
```

    Progress: |||||||||| 100%


```python
"""17.Explain why the backspace escape sequence \b may not work as expected in some environments"""

"""
Not all terminals or consoles handle the backspace character the same way. Some might just move the cursor back without erasing the character, others might ignore it entirely.

The backspace only moves the cursor backward; it doesn't erase the character by itself. To "delete" a character visually, you usually need to print a space after the \b to overwrite it.

Some environments buffer output until a newline is printed, or they treat backspace differently (e.g., Windows Command Prompt behaves differently than Linux terminals)
"""

```




    '\nNot all terminals or consoles handle the backspace character the same way. Some might just move the cursor back without erasing the character, others might ignore it entirely.\n\nThe backspace only moves the cursor backward; it doesn\'t erase the character by itself. To "delete" a character visually, you usually need to print a space after the \x08 to overwrite it.\n\nSome environments buffer output until a newline is printed, or they treat backspace differently (e.g., Windows Command Prompt behaves differently than Linux terminals)\n'




```python
"""18.Create a string that includes an audible beep \a and test if the beep plays on your system"""

str18 = "\aShow Time!"
print("Show starting...")
for i in range(10, 0, -1):
    print(i)

print(str18)

"""If your terminal or console supports it and system sound is enabled, you’ll hear a beep.
Otherwise, it might just silently display the message without the beep."""
```

    Show starting...
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Show Time!
    




    'If your terminal or console supports it and system sound is enabled, you’ll hear a beep.\nOtherwise, it might just silently display the message without the beep.'




```python
"""19.Write a program that prints a dialogue between two people using newline and tab escape sequences for formatting"""

# Get user input for a dialogue between two people
name1 = input("Enter name of Person 1: ")
name2 = input("Enter name of Person 2: ")

line1 = input(f"What does {name1} say? ")
line2 = input(f"What does {name2} reply? ")
line3 = input(f"What does {name1} say next? ")
line4 = input(f"What does {name2} say next? ")

# Format and print the dialogue using \n and \t
dialogue = f"\n\t{name1}: {line1}\n\t{name2}: {line2}\n\t{name1}: {line3}\n\t{name2}: {line4}"

print("\nConversation:")
print(dialogue)
```

    Enter name of Person 1:  sai
    Enter name of Person 2:  ram
    What does sai say?  hello
    What does ram reply?  hi
    What does sai say next?  how r u
    What does ram say next?  im good
    

    
    Conversation:
    
    	sai: hello
    	ram: hi
    	sai: how r u
    	ram: im good
    


```python
"""20.Explain how escape sequences affect the length of a string. Write code to demonstrate your explanation"""
"""Escape sequences (like \n, \t, \\, etc.) are each counted as a single character in the actual string, 
even though they may consist of two characters in the code"""

str20 = "SaiRam\nHello\t!"
len(str20)
```




    14




```python
"""21.Write a Python program that reads a string input from the user and replaces all newline escape sequences with a space"""

str21 = input("Enter a string (use '\\n' for newlines): ")

str21_new = str21.replace('\\n',' ')

print(str21_new)
```

    Enter a string (use '\n' for newlines):  sai\nhello\nram
    

    sai hello ram
    


```python
"""22.Create a function that takes a multiline string and prints each line prefixed with a line number using escape sequences """

def multiline(string):
    str_new = string.split('\n')
    len_str = len(str_new)
    for i in range(len_str):
        print(f"{i+1} - {str_new[i]}")

str22 = """Hello
Sairam
How are you
Learning Python"""

multiline(str22)

```

    1 - Hello
    2 - Sairam
    3 - How are you
    4 - Learning Python
    


```python
"""23.Write a program that simulates a simple console clock updating every second using carriage return \r """

import time

while True:
    print("\r" + time.strftime("%H:%M:%S"), end="")
    time.sleep(1)
```

    20:10:04


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[23], line 7
          5 while True:
          6     print("\r" + time.strftime("%H:%M:%S"), end="")
    ----> 7     time.sleep(1)
    

    KeyboardInterrupt: 



```python
"""24.Write code that demonstrates how to escape backslashes correctly in regular expressions within strings """

import re

# Pattern to match a backslash
pattern = r"\\"

# Text contains one backslash
text = r"\\hello sairam brother"

# Search for backslash
print(re.search(pattern, text))
```

    <re.Match object; span=(0, 1), match='\\'>
    


```python
"""25.Explain and demonstrate how combining escape sequences can be used to format complex output (e.g., tables with indents and line breaks) """
print("Subjects List:\n\t\t- Maths\n\t\t- Science\n\t\t- English\n")
print("Reminder:\n\tDon't forget to enroll")

"""\n creates new lines.\t adds an indent (tab)"""
```

    Subjects List:
    		- Maths
    		- Science
    		- English
    
    Reminder:
    	Don't forget to enroll
    




    '\n creates new lines.\t adds an indent (tab)'




```python
"""26.Create a program that logs errors by printing error messages with a beep sound \a and formatting using tabs and newlines """
def log_error(error_code, message):
    print(f"\a\n\t[ERROR {error_code}]\n\t{message}\n")


log_error(404, "Page not found")
log_error(500, "Internal server error")
log_error(401,"Authentication failed")
```

    
    	[ERROR 404]
    	Page not found
    
    
    	[ERROR 500]
    	Internal server error
    
    
    	[ERROR 401]
    	Authentication failed
    
    


```python
"""27.Write a program to clean a string of all escape characters and print the raw text only"""
escape_list = ['\n', '\t', '\r', '\a', '\b', '\f', '\v', '\\']
str27 = "\\hello sairam\b brother\t\a"
str27_copy = str27
for i in str27:
    if i in escape_list:
        str27_copy = str27_copy.replace(i,'')
print(str27_copy)
```

    hello sairam brother
    


```python
"""28.Implement a text animation in the console using backspace \b to delete characters and rewrite them"""
str28 = input("Enter a text: ")

import time


# Print one character at a time
for i in range(len(str28)):
    print(str28[i], end="")
    time.sleep(1)

# Erase the text one character at a time
for i in range(len(str28)):
    print("\b", end="")
    time.sleep(1)

# Print one character at a time
for i in range(len(str28)):
    print(str28[i], end="")
    time.sleep(1)
```

    Enter a text:  sairam
    

    

    sairam


```python
"""29.Write a program that counts the number of escape sequences in a given string and outputs their types"""

escape_types = {
    r'\n': 'Newline',
    r'\t': 'Tab',
    r'\r': 'Carriage Return',
    r'\a': 'Bell (Beep)',
    r'\b': 'Backspace',
    r'\f': 'Form Feed',
    r'\v': 'Vertical Tab',
    r'\\': 'Backslash',
    r'\"': 'Double Quote',
    r"\'": 'Single Quote',
}

str29 = r"\\sairam\b\nbrother\t\a\'"

for esc in escape_types:
    count = str29.count(esc)
    if count > 0:
        print(f"{esc} - {count} : {escape_types[esc]}")
```

    \n - 1 : Newline
    \t - 1 : Tab
    \a - 1 : Bell (Beep)
    \b - 1 : Backspace
    \\ - 1 : Backslash
    \' - 1 : Single Quote
    


```python
"""30.Create a program that takes a file path input and converts it to a raw string format, escaping necessary characters"""

str30 = input("Enter a file path: ")

# Convert and print as raw-style string
print('\nRaw string version:')
print('r"' + str30.replace('\\', '\\\\') + '"')
```

    Enter a file path:  c:\sairam\folder
    

    
    Raw string version:
    r"c:\\sairam\\folder"
    


```python

```
