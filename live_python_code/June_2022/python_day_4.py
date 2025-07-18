# # 12.6.2022
# # Day4 - Sunday
# # Slicing in Lists and Strings
# # Reference Video : https://www.youtube.com/watch?v=ajrtAuDg3yw

# List of Topics :
# Slicing in detail... complete explanation
# Escape sequences
# '\n' - Newline character
# '\r' - Return character
# '\b' - Backspace character
# '\' - Backslash character
# '\”' - Double quote character
# '\’' - Single quote character
# '\t' - Tab character
# '\a' - Alarm character
# Exercise - 6
# Conditional statements
# If
# If else
# Nested If elif else
# Loops
# While


# # Slicing in Lists and Strings
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# #         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

# # slicing syntax : my_list[start:end:step]

# start = 3
# end = 8
# step = 1
# print(my_list[start:end:step])
# # prints elements 3,4,5,6,7

# print(my_list[3:8:1])
# # prints elements 3,4,5,6,7

# print(my_list[3:8])
# # prints elements 3,4,5,6,7

# print(my_list[-7:-2])
# # prints elements 3,4,5,6,7

# print(my_list[1:-2])
# # [1, 2, 3, 4, 5, 6, 7]

# print(my_list[1:8])
# # [1, 2, 3, 4, 5, 6, 7]

# print(my_list[1:9])
# # [1, 2, 3, 4, 5, 6, 7, 8]

# print(my_list[1:])
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(my_list[0:])
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(my_list[:])
# #print all elements 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# print(my_list[:])
# #print all elements 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# start = 0
# end = 7
# step = 2
# print(my_list[start:end:step])
# # [0, 2, 4, 6]
# # ending index is not included

# # print(my_list[0:7:0])
# # Error : ValueError: slice step cannot be zero

# print(my_list[-1:2:-1])
# # [9, 8, 7, 6, 5, 4, 3]

# print(my_list[2:-1:-1])
# # []

# print(my_list[-2:1:-1])
# # [8, 7, 6, 5, 4, 3, 2]

# print(my_list[-2:1:-2])
# # [8, 6, 4, 2]

# print(my_list[::-1])
# # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# print(my_list[::-2])
# # [9, 7, 5, 3, 1]

# print(my_list[::])
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Let's work on strings now
# # sample_url = 'http://coreyms.com'
# # print sample_url

# # Reverse the url
# # print sample_url[::-1]

# # # Get the top level domain
# # print sample_url[-4:]

# # # Print the url without the http://
# # print sample_url[7:]

# # # Print the url without the http:// or the top level domain
# # print sample_url[7:-4]

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# numbers = "0123456789"

# # [start:stop:step]

# print(numbers[2:6]) #[2, 3, 4, 5]
# print(numbers[1:8]) #[1, 2, 3, 4, 5, 6, 7]
# print(numbers[2:6:1]) #[2, 3, 4, 5]
# print(numbers[1:8:1]) #[1, 2, 3, 4, 5, 6, 7]
# print(numbers[2:6:2]) #[2, 4]
# print(numbers[1:8:2]) #[1, 3, 5, 7]

# 2345
# 1234567
# 2345   
# 1234567
# 24     
# 1357

# print(numbers[2:6:3])#[2, 5]
# print(numbers[1:8:3])#[1, 4, 7]

# print(numbers[-8:-4]) #[2, 3, 4, 5]
# print(numbers[-9:-2]) #[1, 2, 3, 4, 5, 6, 7]

# print(numbers[2:6:-1])
# print(numbers[-1]) #10th element of the list (reverse direction)
# print(numbers[9]) #10th element of the list (forward direction)
# print(numbers[10]) #index-error

# print(numbers[0:10]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[2:-9]) #[]
# print(numbers[2:-9:-1]) #[2]
# print(numbers[2:0:-1]) #[2, 1]
# print(numbers[2:6:-1]) #[]

# [start:stop:step]
# print(numbers[::]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[:]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[2::]) #[2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[:9:]) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#print(numbers[::-2])#[9, 7, 5, 3, 1]

# print(numbers[::-3]) #[9, 6, 3, 0]
# print(numbers[::-1])
# print(numbers[-10:-10:-1])#[]
# print(numbers[0:8:-1])#[]


# my_string = "python_training"
# print(my_string[::-1])

# my_string = "water_bottle"
# my_string = my_string[:5] + '.' + my_string[6:]
# print(my_string) #water.bottle

# my_string.replace('_','.')
# my_string.upper()
# my_string = my_string.lower()
# print(my_string.upper())

# welcome_string = "om sri sai\"s ram"
# welcome_string = 'om sri sai\'s ram'
# # welcome_string = "om sri sai"s ram"

# # print("om sri sai\"s ram")
# # SyntaxError: unterminated string literal (detected at line 163)
# print(welcome_string)

# print("He's \"very good\" boy.\n")

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# first_list = [1, 2, 3]
# second_list = [1, 2, 3]

# first_list = second_list

# if first_list == second_list:
#     print("FIRST LIST AND SECOND LIST ARE SAME")
# else:
#     print("FIRST LIST AND SECOND LIST ARE NOT SAME")

# first_list = [1, 2, 3, 4]
# second_list = [1, 2, 3]

# if first_list == second_list:
#     print("FIRST LIST AND SECOND LIST ARE SAME")
# else:
#     print("FIRST LIST AND SECOND LIST ARE NOT SAME")

# a = 34
# b = 35

# if condition1:
#     print("a is greater than b")
# elif condition2:
#     statements
#     statements
#     statements
# else:
# print("we are outside if")

# weight = int(input("give your weight "))
# height = int(input("give your height "))
# if (weight > 70) and (height > 170):
#   print("You have to reduce your weight.")

# weight = int(input("give your weight "))
# height = int(input("give your height "))
# if (weight > 70) or (height > 170):
#   print("You have to reduce your weight.")


numbers_list = [23, 34, 56, 78, 90] 
print("list length:", len(numbers_list))
list_index = 0
while list_index < 5:
    print(numbers_list[list_index])
    list_index = list_index + 1
    print("newer list index : ", list_index)

# list length: 5
# 23
# newer list index :  1
# 34
# newer list index :  2
# 56
# newer list index :  3
# 78
# newer list index :  4
# 90
# newer list index :  5

# for 



