```python
""" 1. variables -> Create two variables, 
first_name and last_name, assign your own name to them, then print the full name on one line"""

first_name = 'SAIRAM'
last_name = 'EMANI'

print(f"{first_name} {last_name}")

```

    SAIRAM EMANI
    


```python
"""2.numeric operators -> Ask the user for two whole numbers and print their sum, difference, product, and quotient."""
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : ')) 

print(f"Sum of {num1} and {num2} = {num1+num2}")
print(f"Difference of {num1} and {num2} = {num1-num2}")
print(f"Product of {num1} and {num2} = {num1*num2}")
print(f"quotient of {num1} and {num2} = {num1//num2}")

```

    Enter first number :  5
    Enter second number :  6
    

    Sum of 5 and 6 = 11
    Difference of 5 and 6 = -1
    Product of 5 and 6 = 30
    quotient of 5 and 6 = 0
    


```python
"""3. assignment operators -> Start with count = 0. Increment it by 1 three times using +=, then print the final value"""

count = 0  # initial assignment
print(f" initial value = {count}")
count += 1 # first increment
print(f" first increment = {count}")
count += 1 # second increment
print(f" second increment = {count}")
count += 1 # third increment
print(f" third increment = {count}")

```

     initial value = 0
     first increment = 1
     second increment = 2
     third increment = 3
    


```python
"""4. comparison operators -> Input an age and print True if the person is at least 18, otherwise False"""
age = float(input('Enter Age : ')) # read age
if age >= 18 : # check if age is atleast 18
    print("TRUE")
else:
    print("FALSE")

```

    Enter Age :  22
    

    TRUE
    


```python
"""5.logical operators -> Read two Boolean values (e.g., True/False) and print the results of and, or, and not on them"""
bool1 = input("Enter first boolean value : ") 

# input will be read as string so need to reassign as boolean value
if bool1 == "True":
    bool1 = True
if bool1 == "False":
    bool1 = False
    
bool2 = input("Enter Second boolean value : ")
# input will be read as string so need to reassign as boolean value

if bool2 == "False":
    bool2 = False
if bool2 == "True":
    bool2 = True

# Now we compare the re assigned boolean values
b1 = bool1 and bool2
print(f"{bool1} and {bool2} =" ,b1)

b2 = bool1 or bool2
print(f"{bool1} or {bool2} =" ,b2)

b3 = not bool1
print(f"not {bool1} =" ,b3)

b4 = not bool2
print(f"not {bool2} =" ,b4)




```

    Enter first boolean value :  True
    Enter Second boolean value :  False
    

    True and False = False
    True or False = True
    not True = False
    not False = True
    


```python
"""6. boolean type -> Store 0, '', and 42 in a list. Loop through the list and print whether each element is truthy or falsy"""

list = [0,'',42] # creating a list with the 3 elements

for i in list:
    if i:
        print(f" {i} is truthy")
    else:
        print(f" {i} is falsy")
```

     0 is falsy
      is falsy
     42 is truthy
    


```python
"""7.bitwise operators -> Given two integers (e.g., 5 and 3), print their bitwise AND (&) and OR (|) """

number1 = 6
number2 = 4

print(f"bitwise and of {number1}, {number2} is  {number1 & number2}")
print(f"bitwise or of {number1}, {number2} is  {number1 | number2}")
```

    bitwise and of 6, 4 is  4
    bitwise or of 6, 4 is  6
    


```python
"""8.identity operators -> Create two identical lists a = [1,2] and b = [1,2]. Print the results of a is b and a == b """
a = [1,2] # creating a list a with 1,2 as elements
b = [1,2] # creating a list b with 1,2 as elements

print(" a is b :",a is b)
print(" a == b :",a==b)
```

     a is b : False
     a == b : True
    


```python
"""9.membership operators -> Ask the user for a letter and print whether that letter appears in the word "python" """

letter = input('enter a letter :') # read a letter from user input
if letter in "python":
    print("letter present in python")
else:
    print("letter not present in python")

```

    enter a letter : y
    

    letter present in python
    


```python
"""10.input() -> Prompt for a user’s favorite color and then greet them: “Your favorite color is …“ """

color = input("enter your favourite color :")

print(f"Your favorite color is … {color}")
```

    enter your favourite color : orange
    

    Your favorite color is … orange
    


```python
"""11. print() formatting -> Print the numbers 1 to 5 on one line separated by commas using a single print() call"""
print(f"{1}, {2}, {3}, {4}, {5}")
```

    1, 2, 3, 4, 5
    


```python
"""12. decomposition / functions -> Write a function square(n) that returns n*n and call it for numbers 1–5, printing each result"""
# create function square for calculating and returning square of number
def square(n):
    return n*n
    
print(f"square of {1} is {square(1)}")
print(f"square of {2} is {square(2)}")
print(f"square of {3} is {square(3)}")
print(f"square of {4} is {square(4)}")
print(f"square of {5} is {square(5)}")

```

    square of 1 is 1
    square of 2 is 4
    square of 3 is 9
    square of 4 is 16
    square of 5 is 25
    


```python
"""13. indentation -> Use a for loop to print a 5-row left-aligned triangle of * characters (1 on first row, 5 on last)"""
st = "*" # initialise * to a string variable
for i in range(5):
    print(st*(i+1)) # print string variables (i+1) times, with i from 0 to 4 
```

    *
    **
    ***
    ****
    *****
    


```python
"""14.line continuation -> Calculate (3 + 4 + 5 + 6 + 7) on multiple lines using \ for continuation, then print the total."""

sumval = 3 + \
    4 + \
    5 + \
    6 + \
    7

print(sumval)
```

    25
    

    <>:1: SyntaxWarning: invalid escape sequence '\ '
    <>:1: SyntaxWarning: invalid escape sequence '\ '
    C:\Users\SaiRam\AppData\Local\Temp\ipykernel_97596\2481268010.py:1: SyntaxWarning: invalid escape sequence '\ '
      """14.line continuation -> Calculate (3 + 4 + 5 + 6 + 7) on multiple lines using \ for continuation, then print the total."""
    


```python
"""17.integers -> Ask for an integer and print its square using the exponent operator ** """

_number = int(input('Enter an integer'))

print(f" square of {_number} is {_number**2}")
```

    Enter an integer 6
    

     square of 6 is 36
    


```python
"""18.floats -> Read a temperature in Celsius (float) and convert it to Fahrenheit using the formula F = C*9/5 + 32 """

temperature = float(input('Enter temperature in Celsius : '))

_farenheit_temperature = temperature * 9/5 + 32
print(f"Farenheit value of {temperature} Celsius is  : {_farenheit_temperature}") 
```

    Enter temperature in Celsius :  65
    

    Farenheit value of 65.0 Celsius is  : 149.0
    


```python
"""19.comparison + logical -> Input three numbers and print True if they are in strictly increasing order (e.g., 2 < 5 < 9)"""
_num1 = int(input('enter 1st number :'))
_num2 = int(input('enter 2nd number :'))
_num3 = int(input('enter 3rd number :'))

if _num1 < _num2 and _num2 < _num3:
    print(True)
else: 
    print(False)
```

    enter 1st number : 3
    enter 2nd number : 5
    enter 3rd number : 7
    

    True
    


```python
"""20. numeric operators & change-maker -> Ask for an amount of rupees less than 100 and 
show how many ₹50 notes and ₹10 coins are needed to make that amount (use // and %)"""

# Ask the user for input of < 100 rupees
rupees_amount = int(input("Enter an rupees amount less than 100 : "))

if rupees_amount < 100:
    notes_50 = rupees_amount // 50        # Number of rupees 50 notes
    remaining_amount = rupees_amount % 50 # remaining amount after checking rupees 50 notes
    coins_10 = remaining_amount // 10     # Number of rupees 10 coins
    
    print(f"50 rupees notes: {notes_50}")
    print(f"10 rupees coins: {coins_10}")

```

    Enter an rupees amount less than 100 :  99
    

    50 rupees notes: 1
    10 rupees coins: 4
    

##### 
