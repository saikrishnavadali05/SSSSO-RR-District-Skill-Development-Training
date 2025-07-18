Basic


```python
#1.Write a program to create a list of numbers from 1 to 10 using the range() function
n_list = [*range(1,11)]
print(n_list)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    


```python
#2.Create a tuple with the names of five fruits and print the third fruit
fruit_tupple = ('apple','mango','grape','orange','kiwi')
print(fruit_tupple[2])
```

    grape
    


```python
#4.Create a set with five unique integers and print its length
my_set = {*range(1,6)}
print(my_set)
print(len(my_set))
```

    {1, 2, 3, 4, 5}
    5
    


```python
#6.Convert a list of numbers to a tuple and print the tuple.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tupple = tuple(my_list)
print(my_tupple)
```

    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    


```python
#10.Create a set, add two elements to it, and check if a specific element exists in the set
my_set1 = set()

# Add two elements
my_set1.add(10)
my_set1.add(20)

# Check if a specific element exists
element_to_check = 10

# Print results
print("Set:", my_set1)
if element_to_check in my_set1:
    print(f"{element_to_check} exists in the set.")
else:
    print(f"{element_to_check} does not exist in the set.")
```

    Set: {10, 20}
    10 exists in the set.
    

Intermediate Questions


```python
#11. Write a function that returns a list of even numbers from 1 to 50 using range() and list comprehension
print([num for num in range(1, 51) if num % 2 == 0])
```

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    


```python
#12.Create a dictionary where keys are numbers from 1 to 5 and values are their squares

my_dict ={}
for i in range(1,6):
    my_dict[i] = i**2
print(my_dict)
```

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    


```python
#16.Create a function that accepts a dictionary and returns a list of keys sorted alphabetically.

def sort_keys(input_dict):
    return sorted(input_dict.keys())


my_input_dict = {
    "banana": 3,
    "apple": 5,
    "cherry": 2
}

print(sort_keys(my_input_dict))
```

    ['apple', 'banana', 'cherry']
    


```python
#17.Write code to convert a string to a list of characters and then to a set to remove duplicates

string17 = input("enter string: ")
print(  set(  list(string17)  )    )
```

    enter string:  sairam around
    

    {'s', 'u', ' ', 'd', 'i', 'a', 'o', 'm', 'n', 'r'}
    


```python
#19. Use a list and dictionary to count the frequency of each character in a given string

text = input ("enter text: ")
# Convert string to list of characters
char_list = list(text)

# Create an empty dictionary to store frequency
char_freq = {}

# Count frequency of each character
for char in char_list:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Print the result
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")
```

    enter text:  hello sairam how are you
    

    Character frequencies:
    'h': 2
    'e': 2
    'l': 2
    'o': 3
    ' ': 4
    's': 1
    'a': 3
    'i': 1
    'r': 2
    'm': 1
    'w': 1
    'y': 1
    'u': 1
    

Advanced Questions


```python
#21. Implement a function to reverse the keys and values of a dictionary and return a new dictionary

def dict_rev(inputdict):
    rev_dict = {}
    for i in inputdict.keys():
        rev_dict[inputdict[i]] = i
    return rev_dict

input_dict = {
    "hello" : 123,
    "sairam" : 456}

print(dict_rev(input_dict))
        
```

    {123: 'hello', 456: 'sairam'}
    


```python
# 23.Create a nested dictionary representing a student's details (name, subjects, and scores) and print the average score

student = {
    "name": "Sairam",
    "subjects": {
        "Math": 85,
        "English": 92,
        "Science": 80,
        "History": 75
    }
}

# Calculate average score
scores = student["subjects"].values()
average_score = sum(scores) / len(scores)

# Print results
print(f"Student Name: {student['name']}")
print(f"Average Score: {average_score}")
```

    Student Name: Sairam
    Average Score: 83.0
    


```python
#24.Write a function that finds common elements in two lists using set operations and returns them sorted
my_list1 = [1,2,3,4,5,6]
my_list2 = [2,5,8,9]

sorted(set(my_list1).intersection(set(my_list2)))
```




    [2, 5]




```python
#28.Create a function to perform deep copy of a dictionary containing nested dictionaries without using copy.deepcopy()
def dict_deepcopy(d):
    result = {}
    for key in d:
        if type(d[key]) is dict:
            result[key] = dict_deepcopy(d[key])  # Recursive copy
        else:
            result[key] = d[key]
    return result

# input dictionary
original = {
    "name": "Bob",
    "info": {
        "age": 30,
        "scores": {"math": 95, "english": 88}
    }
}

copy_dict = dict_deepcopy(original)

# Change original to check
original["info"]["scores"]["math"] = 100

print("Original:", original)
print("Copy:", copy_dict)
```

    Original: {'name': 'Bob', 'info': {'age': 30, 'scores': {'math': 100, 'english': 88}}}
    Copy: {'name': 'Bob', 'info': {'age': 30, 'scores': {'math': 95, 'english': 88}}}
    


```python
#30. Implement a generator function that yields tuples of (index, value) for a list, mimicking enumerate()

def my_enumerate_fuction(lst):
    for i in range(len(lst)):
        yield (i, lst[i])

# Example usage
my_list_input = ['hello', 123, '456']
for index, value in my_enumerate_fuction(my_list_input):
    print(index, value)
```

    0 hello
    1 123
    2 456
    


```python

```
