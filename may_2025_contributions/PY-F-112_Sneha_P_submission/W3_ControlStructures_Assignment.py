#Basic Level ---------------------------------
#1.Write a Python program to check if a number is positive, negative, or zero using if statement.
number = input("Enter a number: ")
try:
    num = float(number)
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
except ValueError:
    print("Invalid input or no input given")
#2.Write a program to find the largest of two numbers using if-else.
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")
try:
    n1=float(num1)
    n2=float(num2)

    if n1 > n2:
        print("The largest number is:", n1)
    else:
        print("The largest number is:", n2)
except ValueError:
     print("Invalid input or no input given")
#3.Write a program to print all numbers from 1 to 10 using a while loop.
i = 1
print("The numbers from 1 to 10:")
while i <= 10:
    print(i)
    i += 1
#4.Print all even numbers between 1 and 20 using a for loop.
print("The even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i)
#5.Write a program to check whether a number is even or odd.
n= input("Enter a number :")
try:
    num=int(n)
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except ValueError:
    print("Invalid input or no input given")
#6.Write a program to print the multiplication table of a given number using a for loop.
n= input("Enter a number :")
try:
    num=int(n)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input or no input given")
#7.Write a program to find the factorial of a number using a while loop.
n = input("Enter a number: ")
try:
    num=int(n)
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print("Factorial of the number :", factorial)
except ValueError:
    print("Invalid input or no input given")
#8.Write a program to print the first 10 natural numbers using a for loop.
for i in range(1, 11):  
    print(i)
#9.Write a program to find the sum of all numbers from 1 to n, where n is input from the user.
num = input("Enter a number: ")
try:
    n=int(num)
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The sum of numbers from 1 to", n, "is:", total)
except ValueError:
    print("Invalid input or no input given")
#10.Write a program to check if a character is a vowel or consonant using if-else.
try:
    char = input("Enter a letter: ")
    if char.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
except ValueError:
    print("Invalid input or no input given")
#Intermediate Level ---------------------
#11.Write a program to find the largest among three numbers using if-elif-else.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    if a >= b and a >= c:
        print("The largest number is:", a)
    elif b >= a and b >= c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)
except ValueError:
    print("Invalid input or no input given")
#12.Write a program to print all prime numbers between 1 and 100 using for loop and if conditions.
for num in range(2, 101):
    primeno = True
    for i in range(2, num):
        if num % i == 0:
            primeno = False
            break
    if primeno:
        print(num)
#13.Write a program to calculate the sum of digits of a given number using a while loop.
n = input("Enter a number: ")
try:
    num= int(n)
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print("Sum of digits:", sum)
except ValueError:
    print("Invalid input or no input given")
#14.Write a program to reverse a given number using a while loop.
n = input("Enter a number: ")
try:
    num= int(n)
    reversed = 0
    while num > 0:
        reversed = reversed * 10 + num % 10
        num //= 10
    print("Reversed number:", reversed)
except ValueError:
    print("Invalid input or no input given")
#15.Write a program to print a pyramid pattern of stars using nested for loops.
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
#16.Write a program to check if a string is a palindrome using for loop.
str = input("Enter a string: ")
palindromeno = True
for i in range(len(str) // 2):
    if str[i] != str[-(i + 1)]:
        palindromeno = False
        break
if palindromeno:
    print("Palindrome")
else:
    print("Not a palindrome")
#17.Write a program to generate Fibonacci series up to n terms using a while loop.
term = int(input("Enter the number of terms: "))
a, b = 0, 1 
count = 0
print("Fibonacci series:")
while count < term:
    print(a, end=' ')
    a, b = b, a + b 
    count += 1
#18.Write a program to find the GCD (Greatest Common Divisor) of two numbers using while loop.
a = int(input("\nEnter 1st number: "))
b = int(input("Enter 2nd number: "))
while b != 0:
    a, b = b, a % b
print("GCD is:", a)
#19.Write a program to find the factorial of a number using recursion (use if-else for base case).
n = int(input("Enter a number: "))
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
print("Factorial:",factorial(n))
#20.Write a program to count the number of vowels in a given string using a for loop
str = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count += 1
print("Number of vowels in the string :", count)