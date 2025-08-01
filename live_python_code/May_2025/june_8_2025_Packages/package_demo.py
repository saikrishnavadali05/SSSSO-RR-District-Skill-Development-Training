# import Demo_Project
# import may_folder_sample

# print(Demo_Project) # showing (namespace)
# print(Demo_Project.__name__) # dunder
# print(Demo_Project.__file__) # None
# print("-----------------------------")

# print(may_folder_sample) # not showing (namespace)
# print(may_folder_sample.__name__) # dunder
# print(may_folder_sample.__file__) # Path to the file


# Python is pure OOL -> Classes and Objects
# import Demo_Project #Another type of module object #Class is Module; name is Demo_Project
# import Demo_Project.my_utils #Another module object #Class is Module; name is Demo_Project.my_utils


# print(type(Demo_Project))  # <class 'module'>
# print(type(Demo_Project.my_utils))  # <class 'module'>
# Demo_Project.my_utils.greet("Alice")

# correct way to import and use the my_utils module from Demo_Project
# from Demo_Project import my_utils
# my_utils.greet("Alice") # This will work because we imported my_utils from Demo_Project.

# Demo_Project.my_utils.greet("Bob") # This will raise an error because Demo_Project is not defined in this scope.


# This will raise an error
# import Demo_Project.my_utils

# greet("Alice")  # This will raise an error because greet is not defined in this scope.
# my_utils.greet("Alice")  

# from Demo_Project import my_utils
# my_utils.greet("Alice")

# from Demo_Project.my_utils import greet
# greet("Alice")

# import Demo_Project.my_utils as utils
# utils.greet("Bob")

# # import Demo_Project.from_keyword_demo

# import Demo_Project
print(dir(Demo_Project))