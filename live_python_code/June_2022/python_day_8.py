# name_set = {"Harish", "Ramesh", "Suresh"}
# for name_string in name_set:
#     print(name_string)

# # print(name_set[1])
# # name_set[0] = "Ram"
# # print(name_set)

# name_list = list(name_set)
# print(name_list)

# name_tuple = tuple(name_set)
# print(name_tuple)

# name_set = {"Harish", "Ramesh", "Suresh"}
# name_set.add("Mahesh")
# name_set.remove("Harish")
# print(name_set)


# set1 = {1, 4, 9}
# set2 = {9, 15, 2}
# set_result = set2.difference(set1)
# print(set_result)

# duplicate_char_str = 'abracadabra'

# a = set(duplicate_char_str)
# b = set('alacazam')

# print(a)
# print(b)

# # a = list(a)



# Dict notation : {} (curly braces)
# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# print(student)

# print(student['age'])
# print(student['courses'])
# # Dictionary values can be accessed with the help of using corresponing keys in (square brackets) []
# print(student['name'])

# # Finding out the number of keys in dict can be done with the help of len() function
# print(len(student))

# print(student.keys())


# # Print all the keys with keys() method 
# for key in student.keys():
#     print(key)


# Print all the values with values() method 
# for value in student.values():
#     print(value)


# Print both the keys as well as the values with items() method
# for key, value in student.items():
#     print(key, value)

# months = {'fourth_month': 'April', 'second_month': 'Feb', 'fifth_month': 'May', 'first_month': 'Jan'}
# print(months)
# print(months['fourth_month'])

# months[3] = 'March'
# print(months)

# months[100] = "Months are only 12"
# print(months)

# print("keys assigned in dictionary :", months.keys())
# print("values assigned to keys :", months.values())
# del months['second_month']
# print(months)

# print("---------------------------------------")
# for key in months:
    
#     print(key, months[key])

# print("pop(3):", months.pop(3))
# print(months)
# print(months)
# print(5 in months)
# print(3 in months)

# print(months.get('first_month'))
# print(months.get('tenth_month', "Tenth Month value is not present"))
# del months
# months.clear()
# print(months)

# student = {[12, 14, 16] : "ages of 3 students"}
# print(student)

my_dict = {}
# Creating a Dictionary with Mixed keys
my_dict = {'Name': 'Multiple_wishes', 1: [1, 2]}
# print(my_dict['Name']) #'Multiple_wishes'
# print(my_dict[1]) #[1, 2]
my_dict[1] = 5, 6
my_dict[2] = 2, 3, 4

# print(my_dict)

print("\nDictionary with the use of Mixed Keys: ")
my_dict[3] = {'Nested': {1: 'Hyderabad', 2: 'Telangana'}}
print(my_dict)

# output
# {'Name': 'Multiple_wishes', 1: (5, 6), 2: (2, 3, 4), 3: {'Nested': {1: 'Hyderabad', 2: 'Telangana'}}}


# print(my_dict[3]['Nested'][2]) #'Telangana'

# # Creating a Dictionary with dict() method
# my_dict = dict({1: 'Multiple_wishes', 2: 'Py_wishes', 3: 'Company'})
# print("\nDictionary with the use of dict(): ")
# print(my_dict)
# # Creating a Dictionary with each item as a Pair
# my_dict = dict([(1, 'Multiple_wishes'), (2, 'Hyderabad')])
# print("\nDictionary with each item as a pair: ")
# print(my_dict)
cubes = {1: 1, 2: 8, 3: (27,35), 4: 64, 5: 125 }
# for i in cubes:
#     print(cubes[i])
# print("Len = ", len(cubes))

# print("\nby using range statement")
# for i in range(1, 6):
#     print(i ** 3)

cubes[5] = 200
print(cubes)