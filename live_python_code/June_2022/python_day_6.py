# (Day 6) (Sunday) 19.6.2022
# Topics Covered :
# How to contribute on github
# Problem Solving
# For Loop

# Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.

# Take the command line parameter any name you want (C:> C:\Users\Documents\Training\code> python command_line_parameter.py Girish and print in the following paragraph.

# girish_info_string = "Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies."

# word = "Girish"
# mystring = girish_info_string

# if word in mystring: 
#    print('success the word that your searching for is present within your string')

# word = 'Girish is very good boy who helps everyone and also Girish participates in all the sports and cultural meet. Girish hobbies are playing virtual games and also watching movies.'
 
# # returns first occurrence of Substring
# result = word.find('Girish')
# print("Substring 'Girish' found at index:", result)
 
# result = word.find('good')
# print("Substring 'good ' found at index:", result)
 
# # # How to use find()
# # if (word.find('pawan') != -1):
# #     print("Contains given substring ")
# # else:
# #     print("Doesn't contains given substring")


# importing csv module
# import csv
 
# # csv file name
# filename = "aapl.csv"
 
# # initializing the titles and rows list
# fields = []
# rows = []
 
# # reading csv file
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
     
#     # extracting field names through first row
#     fields = next(csvreader)
 
#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
 
#     # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))
 
# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
 
# #  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%10s"%col,end=" "),
#     print('\n')


## For loop

# two_word_string = "MultipleWishes"

# for ch_idx, ch in enumerate(two_word_string, start=0):
    
#     if ch_idx > 8:
#         print(ch)
#         print(ch_idx)
#     else:
#         print("waiting for ch_idx to be greater than 8")

# #tuples
# #lists
# #dictionaries..

# numbers_list = (23, 56, 89, 100)

# for n in numbers_list:
#     print(n)

s = "Multiple_wishes"
"""
Name s is attached to 'Multiple_wishes' string. When you call str(s) the
interpreter puts 'Multiple_wishes' instead of s and then calls str('Multiple_wishes').
"""
# print(str(s))
# print(repr(s))

# print(range(1,7))
# range(1,7) = 1,2,3,4,5,6
for x in range(1, 7):
    print(x)
    
    print(str(x).rjust(2), str(x*x).rjust(5), sep=":", end=" ")
    # Note use of 'end' in the above
    print(str(x*x*x).rjust(4), end=" ")
    print(str(x*x*x*x).rjust(4), end=" ")
    print(str(x*x).rjust(6))

print()
for x in range(1, 5):
    print('{0:2d} {1:4d} {2:4d}'.format(x, x*x, x*x*x))

print()
print('12'.zfill(10))
print('3.14159265'.zfill(5))
print('-3.14'.zfill(6))
print('{0:2} {1:2} {2:2}'.format('company', 'and', 'Multiple_wishes'))
print()
print("PI value is approximately {0:.5f}".format(3.14159265))
print('{0} is {1}'.format('Country', 'India'))
print('{1} {2} {0}'.format('Country', 'India', 'is'))
print('Our {key} is {data}'.format(key='country', data='india'))
print('{0} {company}'.format('Multiple_wishes', company='dream'))