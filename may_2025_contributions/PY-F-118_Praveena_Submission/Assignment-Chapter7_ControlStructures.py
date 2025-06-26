
# Python Training 2025 - Control Structures
# Description : Python program : Create a list of your 3 favorite books.
# Author : Praveena Kumbum
# Date : 9 Jun 2025

#@@@@@@@@@@@@@@ Basic Level @@@@@@@@@@@@@@
#Write a Python program to check if a number is positive, negative, or zero using if statement.
print("**********************************")
print("Program to to check if a number is positive, negative, or zero using if statement.")
num = int(input("Please enter the number: "))
if num > 0:
    print("Positive Number.")
elif num < 0:
    print("Negative Number.")
else:
    print("Zero")

#Write a program to find the largest of two numbers using if-else.
print("\n\n****************************")
print("Program to find the largest of two numbers using if-else.")
i = 1
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")


#Write a program to print all numbers from 1 to 10 using a while loop.
print("\n\n******************************")
print("Program to print the numbers from 1 to 10 using while loop.")
i = 1
while i < 11:
    print(i, end =' ')
    i +=1

#Print all even numbers between 1 and 20 using a for loop.
print("\n\n******************************")
print("Program to print all even numbers between 1 and 20 using a for loop.")
for i in range(1,21):
    if i % 2 == 0:
        print(i,end =' ')

#Write a program to check whether a number is even or odd.
print("\n\n******************************")
print("Program to check whether a number is even or odd,")
num = int(input("Please enter the number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


#Write a program to print the multiplication table of a given number using a for loop.
print("\n\n******************************")
print("Program to print the multiplication table of a given number using a for loop.")
num = int(input("Please enter the number for which multiplication table is needed: "))

print(f"Multiplication table of {num}:\n")
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")


#Write a program to find the factorial of a number using a while loop.
print("\n\n******************************")
print("Program to find the factorial of a number using a while loop.")
num = int(input("Please engter the number for which factorial has to be finded : "))

factorial = 1
i = 1
while i <= num:
    factorial *= i
    i +=1

print(f"Factorial of {num} is : {factorial}.")

#Write a program to print the first 10 natural numbers using a for loop.
print("\n\n******************************")
print("Program to print the first 10 natural numbers using a for loop.")

for i in range(1,11):
    print(i,end =' ')


#Write a program to find the sum of all numbers from 1 to n, where n is input from the user.
print("\n\n******************************")
print("Program to find the sum of all numbers from 1 to n, where n is input from the user.")

n = int(input("Please input the number n : "))
sum = 0
for i in range(1, n+1):
    sum +=i
print(f"sum of all the numbers from 1 to {n} is : ", {sum})


#Write a program to check if a character is a vowel or consonant using if-else.
print("\n\n******************************")
print("Program to check if a character is a vowel or consonant using if-else.")

Vowel = ['a','e','i','o','u']
Character = input("Please input the character : ").lower()
if Character in Vowel:
    print("Vowel")
else:
    print("Consonant")



#@@@@@@@@@@@@@@ Intermediate Level @@@@@@@@@@@@@@
#Write a program to find the largest among three numbers using if-elif-else.
print("\n\n******************************")
print("Program to find the largest among three numbers using if-elif-else.")

num1 = float(input("Please enter the first number : "))
num2 = float(input("Please enter the Second number : "))
num3 = float(input("Please enter the third number : "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"\nThe largest number among {num1}, {num2}, {num3} : {largest}")

#Write a program to print all prime numbers between 1 and 100 using for loop and if conditions.
print("\n\n******************************")
print("Program to print all prime numbers between 1 and 100 using for loop and if conditions.")

for num in range (2,101):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')


#Write a program to calculate the sum of digits of a given number using a while loop.
print("\n\n******************************")
print("Program to calculate the sum of digits of a given number using a while loop.")

num = int(input("Please enter the number : "))
sum = 0
digits = set(str(num))

for digit in digits:
    sum += int(digit)

print(f"sum of digits of {num} is : {sum}")


#Write a program to reverse a given number using a while loop.
print("\n\n******************************")
print("Program to reverse a given number using a while loop.")

num = int(input("Please enter the number : "))
Reverse_num = 0

while num > 0:
    Reverse_num = (Reverse_num * 10) + num % 10
    num = num // 10
print(f"Reverse of given number is : {Reverse_num}")


#Write a program to print a pyramid pattern of stars using nested for loops.
print("\n\n******************************")
print("Program to print a pyramid pattern of stars using nested for loops.")

n = int(input("Please enter the number of rows of starts to be printed."))

for i in range(1, n + 1):
    #print Spaces
    for j in range(n - i):
        print(" ", end="")
    #print stars
    for k in range(2*i-1):
        print("*",end = "")
    print()

#Write a program to check if a string is a palindrome using for loop.
print("\n\n******************************")
print("Program to check if a string is a palindrome using for loop.")

str = input("Please input the string to check if its Palindrome or not : ")

is_Palindrome = True

for i in range(len(str) // 2):
    if str[i] != str[-(i+1)]:
        is_Palindrome = False
        break

if is_Palindrome:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")

#Write a program to generate Fibonacci series up to n terms using a while loop.
print("\n\n******************************")
print("Program to generate Fibonacci series up to n terms using a while loop.")

n = int(input("Please enter the number : "))

a = 0
b = 1

print("Fibonacci series : ")

for i in range(n):
    print(a, end = " ")
    next_term = a + b
    a = b
    b = next_term

#Write a program to find the GCD (Greatest Common Divisor) of two numbers using while loop.
print("\n\n******************************")
print("Program to find the GCD (Greatest Common Divisor) of two numbers using while loop.")

num1 = int(input("Please enter the first number : "))
num2 = int(input("Please enter the second number : "))

small = min(num1,num2)

while small > 0:
    if num1 % small == 0 and num2 % small == 0:
        print("Greatest Common Divisor(GCD) is : ",small)
        break
    small -=1


print("Greatest Common Divisor is :", small)

#Write a program to find the factorial of a number using recursion (use if-else for base case).
print("\n\n******************************")
print("Program to find the factorial of a number using recursion (use if-else for base case).")

num = int(input("Please enter the number for which factorial is to be found : "))


def Factorial(num):
    if num == 1:
        return num
    else:
        return num * Factorial(num -1)
    
print(f"Factorial of {num} is : ", Factorial(num))
        

#Write a program to count the number of vowels in a given string using a for loop.
print("\n\n******************************")
print("Program to count the number of vowels in a given string using a for loop.")

str = input("Please input the string : ").lower()
Vowels = ['a','e','i','o','u']
count = 0

for i in range(len(str)):
    if str[i] in Vowels:
        count +=1
print(f"Number of vowels in the given string is : {count}.")


#@@@@@@@@@@@@@@ Advanced Level @@@@@@@@@@@@@@
"""Write a program to print the pattern of numbers like:
1
12
123
1234
using nested loops."""

print("\n\n******************************")
print("Program to print the number pattern.")

n = int(input("Please input the number of rows : "))

for i in range(n+1):
    for j in range(1, i+1):
        print(j, end =" ")
    print()

#Write a program to find the sum of even and odd numbers separately from a list of numbers.
print("\n\n******************************")
print("Program to find the sum of even and odd numbers separately from a list of numbers.")

numbers = input("Enter the numbers seperated by comma : ").split(',')
numbers = [int(num) for num in numbers]

Even_sum = 0
Odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        Even_sum += num
    else:
        Odd_sum += num
print(f"Sum of even numbers is {Even_sum}, where as sum of odd numbers is {Odd_sum}")


#Write a program to implement a basic calculator using if-elif-else for operations (+, -, *, /).
print("\n\n******************************")
print("Program to implement a basic calculator using if-elif-else for operations (+, -, *, /).")

num1 = float(input("Please input the first number : "))
num2 = float(input("Please input the second number : "))
Operator = input("Please input the operator (+, -, *, /) : ")

if Operator == '+':
    result = num1 + num2
elif Operator == '-':
    result = num1 - num2
elif Operator == '*':
    result = num1 * num2 
elif Operator == '/':
    if num2 != 0:
        result = num1 / num2
    else: 
        result = "infinity"
else:
    result = "Invalid operator"

print("Result : ",result)

#Write a program to merge two sorted lists into a single sorted list using loops.
print("\n\n******************************")
print("Program to merge two sorted lists into a single sorted list using loops.")

set1 = {5,6,8,2,3,1}
set2 = {11,32,64,1,23}

sorted_set1 = sorted(set1)
sorted_set2 = sorted(set2)
set3 = set(sorted_set1).union(set(sorted_set2))
sorted_set3 = sorted(set3)
print("Final sorted list post merging the two sorted lists is : ", sorted_set3)

#Write a program to find the first n prime numbers using loops.
print("\n\n******************************")
print("Program to find the first n prime numbers using loops.")

n = int(input("Please enter the number of prime numbers needed : "))
count = 0
num = 2

while count < n:
    is_prime = True

    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end =' ')
        count +=1

    num +=1

#Write a program to remove duplicate elements from a list without using set().
print("\n\n******************************")
print("Program to remove duplicate elements from a list without using set().")

original_list = [1,2,3,4,5,2,3,4,6,7,8,9]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("list after removing duplicates is : ",unique_list)


#Write a program to check whether a given year is a leap year or not using control structures.
print("\n\n******************************")
print("Program to check whether a given year is a leap year or not using control structures.")

year = int(input("Please enter the year : "))

if year % 4 == 0:
    if (year % 100 != 0 or year % 400 ==0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")

#Write a program to print all Armstrong numbers between 100 and 999 using nested loops.
print("\n\n******************************")
print("Program to print all Armstrong numbers between 100 and 999 using nested loops.")

for num in range(100, 1000):
    sum_of_cubes = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        cube = 1
        for i in range(3):
            cube *= digit
        sum_of_cubes += cube
        temp = temp // 10
    if num == sum_of_cubes:
        print(num, end =' ')
  

#Write a program to simulate a number guessing game where the user has limited attempts.
print("\n\n******************************")
print("Program to simulate a number guessing game where the user has limited attempts.")

import random

Secret_number = random.randint(1,100)
max_attempts = 5

for attempt in range(1,max_attempts + 1):
    guess = int(input("Please enter your gussed number : "))

    if guess == Secret_number:
        print(f"You have gussed the number in {attempt} attempts.")
        break
    elif guess < Secret_number:
        print("too low. Try again.")
    else:
        print("Too high. Try again.")
    if attempt == max_attempts:
        print(f"You couldnt guess the {Secret_number} number correctly in the alloted number of attempts. Better luck next time.")


#Write a program to print Pascal’s triangle up to n rows using nested loops.
print("\n\n******************************")
print("Program to print Pascal's Triangle.")

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    print(" " * (rows - i), end="")

    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1) 

    print()

