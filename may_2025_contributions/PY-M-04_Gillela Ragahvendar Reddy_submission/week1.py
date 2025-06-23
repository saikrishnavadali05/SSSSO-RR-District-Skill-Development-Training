# 1. Variables - fullname
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name + " " + last_name)

# 2. Numeric operators - sum, difference, product, and quotient of two numbers
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Quotient:", a // b)
else:
    print("Cannot divide by zero")

# 3. Assignment operators - increment count three times
count = 0
while count < 3:
    count += 1
print("Count:", count)

# 4. Comparison operators - check if age is at least 18
age = int(input("Enter age: "))
if age >= 18:
    print("True")
else:
    print("False")

# 5. Logical operators - AND, OR, NOT of two boolean inputs
# Convert input strings to boolean by checking for 'true' (case insensitive)
l1 = input("Enter value 1 (True/False): ").strip().lower() == "true"
l2 = input("Enter value 2 (True/False): ").strip().lower() == "true"
print("Value 1 AND Value 2:", l1 and l2)
print("Value 1 OR Value 2:", l1 or l2)
print("NOT Value 1:", not l1)
print("NOT Value 2:", not l2)

# 6. Boolean type - print items in list using loop
lt = [0, '', 42]
for i in lt:
    if i:
        print(repr(i), "is truthy")
    else:
        print(repr(i), "is falsy")

# 7. Bitwise operators - bitwise AND, OR of two numbers
b1 = int(input("Enter number 1: "))
b2 = int(input("Enter number 2: "))
print("Bitwise AND:", b1 & b2)
print("Bitwise OR:", b1 | b2)

# 8. Identity operators - print identical list checks
a = [1, 2]
b = [1, 2]
print("a is b:", a is b)   # False because they are different objects
print("a == b:", a == b)   # True because contents are equal

# 9. Membership operators - check if a letter is in the word 'python'
w1 = 'python'
lr1 = input("Enter a letter: ")
if lr1 in w1:
    print("Letter", lr1, "is in the word", w1)
else:
    print("Letter", lr1, "is not in the word", w1)

# 10. input() - user favourite color
fav = input("Enter your favourite color: ")
print("Your favourite color is", fav)

# 11. Print formatting - print numbers 1 to 5 in one line with commas
print(1, 2, 3, 4, 5, sep=',')

# 12. Functions - square of numbers
def square(n):
    return n * n

sq = 1
while sq != 6:
    print(square(sq))
    sq += 1

# 13. Indentation - 5 row left aligned triangle
for t in range(1, 6):
    print('*' * t)

# 14. Line continuation - using \ while adding numbers
print(3 + \
      4 + \
      5 + \
      6 + \
      7)

# 15. Pylint basics - simple variable print
P = 1
print(P)

# 16. CLI args - print one word by user only
import sys
if len(sys.argv) == 2:
    print(sys.argv[1])
else:
    print("The program accepts only one word")

# 17. Integers - print square using exponent operator
sqr = int(input("Enter a number: "))
print(sqr ** 2)

# 18. Floats - temperature conversion from Celsius to Fahrenheit
C = float(input("Enter temperature in Celsius: "))
F = (C * 9 / 5) + 32
print(f"{C} Celsius is {F} Fahrenheit")

# 19. Comparison + logical - increasing order of input numbers
N1 = int(input("Enter number1: "))
N2 = int(input("Enter number2: "))
N3 = int(input("Enter number3: "))
if N2 > N1 and N3 > N2:
    print(True)
else:
    print(False)

# 20. Numeric operators & changemakers - calculate the money in 50 rupee notes and 10 rupee coins
Amount = int(input("Enter amount less than 100 rupees: "))
if Amount >= 100 or Amount <= 0:
    print("Enter valid amount below 100")
else:
    Notes = Amount // 50
    Balance = Amount % 50
    Coins = Balance // 10
    print("Number of 50 rupees notes:", Notes)
    print("Number of 10 rupees coins:", Coins)
