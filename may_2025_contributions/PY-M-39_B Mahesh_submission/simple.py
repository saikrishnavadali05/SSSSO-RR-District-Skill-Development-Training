#Write a Python program that prints your name and age on separate lines.

print("My name is B Mahesh.\nI am 22 years old.")

# Use the print() function to display the result of 5 + 7
a = 5 
b = 7 
c = a + b 
print(f"Addition of {a} and {b} = {c}")

#Write a script that prints three lines using a single print() with newline characters.

print("This is one line.\nThis is second line.\nThis is third line.")

multiple_lines = """This is one line.
This is second line.
This is third line."""
print(multiple_lines)               

#Write a program using proper indentation that prints a message if a number is greater than 10.

a = 23
if a > 10:
    print("This nuumber is greater than 10.")
else:
    print("Not")

#Use line continuation (\) to split a long expression over two lines.

total = 100 + 200 + 300 + \
        400 + 500
print("The total is:",total)

#Create a basic script that uses variables and prints them using formatted strings.

name = "Mahesh" 
age = 22
city = "Hyderabad"
print(f"My name if {name},i am {age} years old, and I live in {city}")

#Write a program with nested indentation that prints messages at different levels.

number = 15

if number > 10:
    print("Level 1: The number is greater than 10.")
    
    for i in range(3):
        print(f"  Level 2: Loop {i + 1}")
        
        if i == 1:
            print("    Level 3: i is equal to 1")

