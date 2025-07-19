# Python Classroom Code Day3 - 11.06.2022 - Saturday

# Topics Covered : 
# Variables
# Python Variables
# Common conventions followed for variable names
# Creating good names
# Exercise - 2
# User Input
# Input function
# Command line parameters (arguments)
# Exercise - 3
# Operators
# Numeric
# Assignment
# Comparision
# Logical
# Membership
# Identity
# Exercise - 4
# strings
# Indexing
# Object Identity
# Program using builtin function
# Formatting with .format method
# Important points to remember
# builtin functions, methods of string

# # amount1 = 1000
# # amount2 = 2000
# # amount3 = 3000
# # amount4 = 4000
# # amount5 = 5000

# # AMount1 = 1000
# # AMount2 = 2000
# # AMount3 = 3000
# # AMount4 = 4000
# # AMount5 = 5000


# # amount_sum = amount1 + amount2 + amount3 + amount4 + amount5

# # print("total sum : ", amount_sum)
# # print("data type of amount 4 : ", type(amount4))

# # amountFour = 4000
# # amount_four = 4000

# # a1 = 1000
# # a2 = 2000
# # a3 = 3000
# # a4 = 4000
# # a5 = 5000

# # student_name = "Ramesh"

# # number1 = 5
# # number2 = 10
# # number3 = number2 - number1

# # print(number3)

# # name_of_student = input("What is the name of the student?")
# # print("name of the student : ", name_of_student)

# # first_number = input("Please give the first number:")
# # print("first number : ", first_number)
# # print("first number type: ", type(first_number))

# # first_number = int(first_number)
# # print("first number : ", first_number)
# # print("first number type: ", type(first_number))

# # print("---------------")
# # first_number = float(input("Please give the first number:"))
# # print("first number : ", first_number)
# # print("first number type: ", type(first_number))

# # from sys import argv

# # print("argv list : ", argv)
# # num1 = int(argv[1])
# # num2 = int(argv[2])
# # num3 = int(argv[3])
# # num4 = int(argv[4])
# # addition1 = num1 + num2
# # addition2 = num3 + num4

# # addition1 = num1 // num2
# # addition2 = num3 / num4
# # print("The total addition1 result is", addition1)
# # print("The total addition2 result is", addition2)

# x = 2
# y = 5

# x += y # is same as x = x + y
# print(x)
# # x = x + y
# # print(x)

# x -= y # is same as x = x - y
# x *= y # is same as x = x * y
# x **= y # is same as x = x ** y
# x /= y # is same as x = x / y
# x //= y # is same as x = x // y
# x %= y # is same as x = x % y

# num1 = 25
# num2 = 10

# print(num2 < num1)

# if num2 < num1:
#     print(num2)

# else:
#     print(num1)



# name = "multiple"
# print(name[3])
# print(name[-1])

# name = 'multiple'
# # print(name[3])
# # print(name[-1])
# # print(name[0])
# # print(name[7])
# # print(name[10])

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

# a = 50
# b = a
# print("Id of a variable is",id(a))
# print("Id of b variable is",id(b))
# # Reassigned variable a
# a = 500
# print("Id of a variable is",id(a))
# print("Id of b variable is",id(b))

# str1 = "Multiple_Wishes"
# str2 = "Py_wishes"
# print("Id number for str1 is ", id(str1), "\n" "Id number for str2 is ", id(str2))
# # str1[1] = 'a' # illegal, since strings are (immmutable)

# # # # new string created from old ones
# str1 = str1[:1] + 'i' + str1[6:]

# print("by indexing and adding i str1 is :", str1, str2)
# print("Now str1,str2 id's are: ", id(str1), id(str2))


# Name = "Multiple_Wishes"
# print("Finding the letter index ", Name.index('e'))
# print(Name.index('is'))
# print('a' in Name)
# print(Name.upper(), Name.lower())
# print(Name.replace('p', 'b'))

Symbol = "----"
symbol_attach = Symbol.join(('Multiple_Wishes', 'Hyd', 'India'))
print(symbol_attach)
Name = "Multiple_Wishes"
print("Printing name 3times: ", Name*3, "\n" "Length of name is: ",len(Name))
print(Name[0:10])
Str_name = "hello123"
print("Is Str_name contains numbers: ", Str_name.isalnum(), "\n" "Is string name contains Alphabets: ", Str_name.isalpha())
val = "123"
print(val.isdigit())
Name = "Multiple_Wishes"
print(Name.isalpha())
