Basic Level


```python
# 1. Write a Python program to check if a number is positive, negative, or zero using if statement
number = int(input('Enter Number: '))
if number > 0:
    print("positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

    Enter Number:  -23
    

    Negative
    


```python
#2. Write a program to find the largest of two numbers using if-else.
number1 = int(input('Enter Number: '))
number2 = int(input('Enter Number: '))
if number1 > number2:
    print(f"{number1} is greater")
elif number1 == number2:
    print("Both are equal")
else:
    print(f"{number2} is greater")
```

    Enter Number:  10
    Enter Number:  11
    

    11 is greater
    


```python
#3. Write a program to print all numbers from 1 to 10 using a while loop
numbers = 1
while numbers <=10:
    print(numbers)
    numbers += 1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
#4. Print all even numbers between 1 and 20 using a for loop
for i in range(0,21):
    if i % 2 == 0:
        print(i)
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    


```python
#5. Write a program to check whether a number is even or odd.
number_oe = int(input('Enter Number: '))
if number_oe % 2 == 0:
    print("even")
else:
    print("odd") 
```

    Enter Number:  21
    

    odd
    


```python
#6. Write a program to print the multiplication table of a given number using a for loop
number_t = int(input('Enter Number: '))
for i in range(1,11):
    print(number_t * i)
```

    Enter Number:  2
    

    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    


```python
#7. Write a program to find the factorial of a number using a while loop
number_fac = int(input('Enter Number: '))
if number_fac < 0:
    print("Factorial is not defined for negative numbers.")
elif number_fac == 0:
    print(f"The factorial of {number_fac} is {factorial}")
else:
    factorial = 1
    i = 1
    while i <= number_fac:
        factorial *= i
        i += 1

    print(f"The factorial of {number_fac} is {factorial}")
```

    Enter Number:  4
    

    The factorial of 4 is 24
    


```python
# 8. Write a program to print the first 10 natural numbers using a for loop
natural_limit = int(input('Enter Number: '))
for i in range (1,natural_limit + 1 ):
    print(i)
```

    Enter Number:  10
    

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
# 9. Write a program to find the sum of all numbers from 1 to n, where n is input from the user
number_limit = int(input('Enter Number: '))
sum_number = 0
for i in range(number_limit,0,-1):
    sum_number += i

print(sum_number)
```

    Enter Number:  5
    

    15
    

Intermediate Level


```python
#12. Write a program to print all prime numbers between 1 and 100 using for loop and if conditions
print("Prime numbers between 1 and 100 are:")

for i in range(2, 101):  # Start from 2 because 1 is not prime
    is_prime = True

    for j in range(2, i):  # Check all numbers from 2 to num-1
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
```

    Prime numbers between 1 and 100 are:
    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    31
    37
    41
    43
    47
    53
    59
    61
    67
    71
    73
    79
    83
    89
    97
    


```python
# 13. Write a program to calculate the sum of digits of a given number using a while loop
number_dig = int(input("Enter a number: "))

# Initialize sum
digit_sum = 0

# Use while loop to extract digits
while number_dig > 0:
    digit = number_dig % 10        # Get the last digit
    digit_sum += digit      # Add it to the sum
    number_dig = number_dig // 10         # Remove the last digit

# Display the result
print("Sum of digits is:", digit_sum)
```

    Enter a number:  123
    

    Sum of digits is: 6
    


```python
# 14. Write a program to reverse a given number using a while loop.
number_rev = int(input("Enter a number: "))

reversed_num = 0

# Use while loop to extract digits
while number_rev > 0:
    digit = number_rev % 10        # Get the last digit
    reversed_num = reversed_num * 10 + digit      
    number_rev = number_rev // 10         # Remove the last digit

# Display the result
print("reverse of number is:", reversed_num)
```

    Enter a number:  123
    

    reverse of number is: 321
    


```python
# 15. Write a program to print a pyramid pattern of stars using nested for loops
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```

    Enter the number of rows:  5
    

        *
       ***
      *****
     *******
    *********
    


```python
#17.Write a program to generate Fibonacci series up to n terms using a while loop
fibonacci_limit = int(input("Enter the max limit of fibonaci: "))

# First two Fibonacci numbers
a, b = 0, 1
count = 0

print("Fibonacci series:")

while count < fibonacci_limit:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
```

    Enter the max limit of fibonaci:  10
    

    Fibonacci series:
    0 1 1 2 3 5 8 13 21 34 


```python
#18. Write a program to find the GCD (Greatest Common Divisor) of two numbers using while loop

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

print("GCD is", num1)
```

    Enter first number:  60
    Enter second number:  36
    

    GCD is 12
    

Advanced Level



```python
# 21. Write a program to print all Armstrong numbers between 100 and 999 using nested loops.

for i in range(100,1000):
    sum_of_cubes = 0
    temp = i

    # Extract digits using a while loop (nested inside the for loop)
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10

    if sum_of_cubes == i:
        print(i)
```

    153
    370
    371
    407
    


```python
""" 27. Write a program to print the pattern of numbers like:
1
12
123
1234
using nested loops """

num_rows = int(input("Enter number of rows: "))

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

    Enter number of rows:  4
    

    1
    12
    123
    1234
    


```python
# 28. Write a program to find the first n prime numbers using loops
prime_limit = int(input("Enter limit: "))

for i in range(2,prime_limit+1):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
            print(i)
```

    Enter limit:  20
    

    2
    3
    5
    7
    11
    13
    17
    19
    


```python

```
