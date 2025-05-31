# 1. Write a Python program that prints your name and age on separate lines.
print("Sai Srujan\n25")


#2. Add comments to explain what your program does in Question 1

# Here, In the above program \n is an escape sequence in Python that represents a newline character.
# So, by adding \n after the name, the age will be displayed on new line


#13. Write a script that prints the current year and your expected graduation year using variables.
from datetime import datetime

# Get the current year using datetime
current_year = datetime.now().year

graduation_year = 2027 

print(f"Current Year: {current_year}")
print(f"Expected Graduation Year: {graduation_year}")


#15. Print a formatted string showing your name, department, and college using f-strings.
name = "Sai Srujan"
department = "Automotive Electronics"
college = "BITS-Pilani"

print(f"My name is {name}, I study in the {department} department at {college}.")


#16. Write a program that uses indentation correctly to define a function that prints "Hello!".

def say_hello():
    print("Hello!")

say_hello()

#19 Write a script that contains incorrect indentation. Then correct it and explain the changes.

#Incorrect Indentation Example:
"""
def greet(name):
print(f"Hello, {name}!")
  print("Welcome to the Python world.")

greet("Alice")
"""

#Corrected Version:

def greet(name):
    print(f"Hello, {name}!")
    print("Always think of the Lord")

greet("Sai Srujan")


#20. Compare and demonstrate how print behaves with and without end-line characters (end="").

#Without end-line
print("Hello")
print("World")

#With end-line
print("Hello", end="")
print("World")


#24. Use indentation to structure a decision tree using if-elif-else blocks clearly.

age = 25

if age < 0 or age > 150:
    print("Invalid age. Please enter an age between 0 and 150.")
elif age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")


#25. Use the continuation character in an if-statement condition spanning multiple lines.

age_n = 25
has_id = True
is_member = True

if age_n >= 18 and has_id == True and \
   is_member == True:
    print("Access granted.")
else:
    print("Access denied.")


#26. Create a script with nested loops and use proper indentation to maintain clarity.

for i in range(1, 4):         # Outer loop runs from 1 to 3
    print(f"Outer loop iteration {i}:")
    
    for j in range(1, 4):     # Inner loop runs from 1 to 3
        print(f"  Inner loop iteration {j}")
    
    print() # Blank line for better readability between outer loop iterations
