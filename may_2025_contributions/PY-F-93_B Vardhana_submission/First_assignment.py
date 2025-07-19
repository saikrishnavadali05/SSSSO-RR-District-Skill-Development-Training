#variable
first_name="Vardhana"
last_name="Reddy"
print(first_name+" "+last_name)

#numeric operators
num1=int(input("enter first whole number:"))
num2=int(input("enter second whole number:"))
sum=num1+num2
print("Sum is :"+sum)
Diff=num1-num2
print("Difference is:"+Diff)
mult=num1*num2
print("Product is:"+mult)
if num2 != 0:
    quotient = num1 / num2
    print("Quotient:", quotient)
else:
    print("Quotient: Cannot divide by zero")

#assignment operator
count=0
for i in range(3):
    count += 1
print("Final count:", count)


#comparison operator
age=int(input("Enter age of a person:"))
if(age>=18):
    print(True)
else:
    print(False)


#logical operator
bool1 = input("Enter first Boolean value (True/False): ").strip()
bool2 = input("Enter second Boolean value (True/False): ").strip()
bool1 = bool1.capitalize() == 'True'
bool2 = bool2.capitalize() == 'True'
print("Result of AND:", bool1 and bool2)
print("Result of OR:", bool1 or bool2)
print("Result of NOT on first Boolean:", not bool1)
print("Result of NOT on second Boolean:", not bool2)

#Boolean type
values = [0, '', 42]
for value in values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")


#bitwise operator 
int1=int(input("Enter num1"))
int2=int(input("Enter num2"))
print("Bitwise AND:"+ int1 & int2)
print("Bitwise OR:"+ int1 | int2)


#identity operator
a=[1,2,3,4]
b=[1,2,3,4]
print(a is b) #False because they different objects in memory
print(a==b) #True because both are having same items


#membership operator
letter=input("Enter a any letter:")
print(letter in "python")


#input()
fav_color=input("Enter favorite color:")
print("Your favorite color is "+fav_color)


#print()
print(1,2,3,4,5, sep=",")


#functions
def fun(n):
    return n*n
for i in range(1,6):
    print(fun(i))


#indentation
for i in range(1,6):
    print('*'*i)


#line continuation
total=3+4+5+\
        6+7
print("Total is:" , total)      #as total is int we should use comma for sep,through + we can't concat


#pylint basics
X = 10  #bad_name
print(X)    #get a warning bad variable 
x = 10  # good_name
print(x)

#CLI args
import sys

if len(sys.argv) != 2:
    print("Usage: python echo.py <word>")
else:
    word = sys.argv[1]
    print(word)


#integer
var=int(input("Enter an integer:"))
print(var**2)


#float
Celsius=32.65
F=Celsius*9/5 +32
print(F)


#comparsion +logical
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
print(num1<num2<num3)

#numeric operators &change-maker
amt=int(input("Enter amount less than 100: "))
notes_50=amt//50  #// gives how many complete notes
remaining=amt%50  #%gives remaining amt after using 50 notes
coins_10=amt//10
print("₹50notes",notes_50)
print("₹10coins",coins_10)
