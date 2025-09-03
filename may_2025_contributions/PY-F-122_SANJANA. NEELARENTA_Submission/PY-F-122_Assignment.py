# program 1
first_name = "sai" 
last_name = "ram" 
full_name = first_name + " " + last_name 
print(full_name)

#program 2
# Ask the user for two whole numbers
num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Check for division by zero
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (cannot divide by zero)"

# Print the results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#program 3
# Initialize the count
count = 0

# Increment the count by 1 three times
count += 1
count += 1
count += 1

# Print the final value of count
print("Final value of count is:", count)

#program 4
# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the person is at least 18
is_adult = age >= 18

# Print the result
print(is_adult)

#program 5
# Read two Boolean values as strings
bool1 = input("Enter first boolean (True/False): ")
bool2 = input("Enter second boolean (True/False): ")

# Convert the string inputs to actual Boolean values
bool1 = True if bool1 == "True" else False
bool2 = True if bool2 == "True" else False

# Print the logical operations results
print("AND:", bool1 and bool2)
print("OR:", bool1 or bool2)
print("NOT first boolean:", not bool1)
print("NOT second boolean:", not bool2)

#program 6
# List with values
values = [0, '', 42]

# Loop through each value in the list
for value in values:
    if value:
        print(value, "is truthy")
    else:
        print(value, "is falsy")

#program 7
# Given two integers
num1 = 5
num2 = 3

# Calculate bitwise AND and OR
bitwise_and = num1 & num2
bitwise_or = num1 | num2

# Print the results
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)

#program 8
# Create two identical lists
a = [1, 2]
b = [1, 2]

# Check if a and b are the same object
print("a is b:", a is b)

# Check if a and b have the same content
print("a == b:", a == b)

#program 9
# Ask the user for a letter
letter = input("Enter a letter: ")

# Check if the letter is in "python"
if letter in "python":
    print("Yes, the letter", letter, "is in 'python'.")
else:
    print("No, the letter", letter, "is not in 'python'.")

#program 10
# Ask the user for their favorite color
color = input("What is your favorite color? ")

# Greet the user with their favorite color
print("Your favorite color is", color + "!")

#program 11
print(1, 2, 3, 4, 5, sep=", ")

#program 12
# Define the square function
def square(n):
    return n * n

# Call the function for numbers 1 to 5 and print the results
for i in range(1, 6):
    print("square(", i, ") =", square(i))

#program 13
# Print a left-aligned triangle with 5 rows
for i in range(1, 6):
    print('*' * i)

#program 14
total = 3 + \
        4 + \
        5 + \
        6 + \
        7

print("Total:", total)

#program 17
# Ask the user for an integer
number = int(input("Enter an integer: "))

# Calculate the square using **
square = number ** 2

# Print the result
print("The square of", number, "is", square)

#program 18
# Ask the user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Print the result
print("Temperature in Fahrenheit:", fahrenheit)

#program 19
# Get three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check if they are in strictly increasing order
is_increasing = a < b < c

# Print the result
print("Strictly increasing:", is_increasing)

#program 20
# Ask for an amount less than 100
amount = int(input("Enter an amount less than ₹100: "))

# Calculate ₹50 notes
fifty_notes = amount // 50

# Remaining amount after ₹50 notes
remaining = amount % 50

# Calculate ₹10 coins
ten_coins = remaining // 10

# Print the result
print("₹50 notes needed:", fifty_notes)
print("₹10 coins needed:", ten_coins)

