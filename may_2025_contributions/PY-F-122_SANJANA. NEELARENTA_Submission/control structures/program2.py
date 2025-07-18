#Write a program to find the largest of two numbers using if-else.

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The larger number is: {num1}")
elif num2 > num1:
    print(f"The larger number is: {num2}")
else:
    print("Both numbers are equal.")
