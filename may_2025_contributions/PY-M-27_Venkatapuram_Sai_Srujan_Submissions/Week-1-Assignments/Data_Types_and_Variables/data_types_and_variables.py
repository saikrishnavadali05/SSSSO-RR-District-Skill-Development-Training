#1. Create a variable to store your name, age, and height. Print all three.
name = "Sai Srujan"
age = 25
height = 5.53  # in feet

# Print all three
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")

print() # adding print for new line for the Terminal Output


#7. Use the complex() function to create a complex number and print its real and imaginary parts.

z = complex(4, 7)  # 4 is the real part, 7 is the imaginary part

print("Complex number:", z)

print("Real part:", z.real)
print("Imaginary part:", z.imag)

print() # adding print for new line for the Terminal Output


#21. Write a function that accepts any number and returns its data type.

def check_data_type(value):

    return type(value).__name__

# Example usage
print(check_data_type(10))       # Output: int
print(check_data_type(3.14))     # Output: float
print(check_data_type("hello"))  # Output: str

print() # adding print for new line for the Terminal Output

#23. Write a program to demonstrate dynamic typing in Python.

x = 10              # x is an integer
print("x =", x, "| Type:", type(x).__name__)

x = 3.14            # x is now a float
print("x =", x, "| Type:", type(x).__name__)

x = "Hello"         # x is now a string
print("x =", x, "| Type:", type(x).__name__)

x = [1, 2, 3]       # x is now a list
print("x =", x, "| Type:", type(x).__name__)

x =(1, 2, 3)       # x is now a tuple
print("x =", x, "| Type:", type(x).__name__)

print() # adding print for new line for the Terminal Output


#24. Compare the behavior of == and is for strings and integers.

# For strings

str1 = "hello"
str2 = "hello"
str3 = "".join(["he", "llo"])  # forces a new object

print(str1 == str2)   # True (same value)
print(str1 is str2)   # True (Python optimizes string literals)

print(str1 == str3)   # True (same value)
print(str1 is str3)   # False (different memory objects)

#For Integers

a = 100
b = 100
c = int("100")  # creates new object, but small integers are cached

print(a == b)   # True (same value)
print(a is b)   # True (due to integer caching from -5 to 256)

print(a == c)   # True (same value)
print(a is c)   # True (because 100 is cached)


#For Large Integers
x = 1000
def make_y():
    return 1000

y = make_y()

print(x == y)  # True
print(x is y)  # Now should be False


#printing id of x and y to confirm
print(id(x))
print(id(y))

print() # adding print for new line for the Terminal Output


#25. Create a program that stores a user's profile (name, age, email, etc.) using well-named variables and prints it

# User profile information stored in variables
user_name = "Sai Srujan"
user_age = 25
user_email = "saisrujan137@gmail.com"
user_phone = "+91 707540"
user_city = "Hyderabad"

# Print the user's profile
print("User Profile:")
print("Name:", user_name)
print("Age:", user_age)
print("Email:", user_email)
print("Phone:", user_phone)
print("City:", user_city)

print() # adding print for new line for the Terminal Output


#26. Demonstrate implicit and explicit type conversions with examples.

"""
Implicit Type Conversion (Type Coercion)
Python automatically converts one data type to another without user intervention.

Explicit Type Conversion (Type Casting)
Programmer manually converts a value from one type to another using functions like int(), float(), str(), etc.
"""

# Implicit conversion example
s = 5        # int
a = 2.5      # float

result = s + a   # int + float → float (implicit conversion)
print(result)    # 7.5
print(type(result))  # <class 'float'>


# Explicit conversion example
num_str = "123"
num_int = int(num_str)  # Convert string to integer explicitly

print(num_int)          # 123
print(type(num_int))    # <class 'int'>

# Another example
pi_float = 3.14159
pi_int = int(pi_float)  # Converts float to int by truncation

print(pi_int)           # 3
print(type(pi_int))     # <class 'int'>


print() # adding print for new line for the Terminal Output

#27. Create variables of each primitive data type and store them in a dictionary. Print the dictionary.

# Variables of primitive data types
my_int = 42            # Integer
my_float = 3.14        # Float
my_bool = True         # Boolean
my_str = "Hello"       # String
my_complex = complex(2, 3)  # Complex number

# Store them in a dictionary
primitive_data = {
    "Integer": my_int,
    "Float": my_float,
    "Boolean": my_bool,
    "String": my_str,
    "Complex": my_complex
}

# Print the dictionary
print(primitive_data)

print() # adding print for new line for the Terminal Output



#29. Track and display changes to a variable over time using reassignment.

# Initial value
counter = 0
print("Initial value:", counter)

# First change
counter = 5
print("After first change:", counter)

# Second change
counter = counter + 10
print("After second change:", counter)

# Third change
counter -= 3
print("After third change:", counter)
