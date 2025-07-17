#Intermediate Questions--------------------
#11.Write a function that returns a list of even numbers from 1 to 50 using range() and list comprehension.
print("Even numbers from 1 to 50:")
def evennumbers():
    return [x for x in range(1, 51) if x % 2 == 0]
print(evennumbers())
#12.Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
print("Squares of numbers from 1 to 5:")
squares = {x: x**2 for x in range(1, 6)}
print(squares)
#13.Given a tuple of integers, write code to find the sum of all elements.
numbers = (1,3,5,7,11,13,17,19) 
total = sum(numbers)
print("Sum of elements:", total)
#14.Write a function to merge two sets and return the resulting set without duplicates.
set1 = {2, 4, 6}
set2 = {6, 8, 10}
def merge_sets(set1, set2):
    return set1.union(set2)

result = merge_sets(set1,set2)
print("Merged set:", result)
#15.Use an OrderedDict to maintain and print the order of insertion of items added dynamically in a loop.
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for k, v in od.items():
    print(k, v)
#16.Create a function that accepts a dictionary and returns a list of keys sorted alphabetically.
def listsortedkeys(d):
    return sorted(d.keys())

diction = {'banana': 3, 'apple': 5, 'cherry': 2}
sortedkeys = listsortedkeys(diction)
print(sortedkeys)
#17.Write code to convert a string to a list of characters and then to a set to remove duplicates.
str = "Sairam to all"
listofchar = list(str)
chartoset = set(listofchar)
print("Original List:", listofchar)
print("Unique Characters Set:", chartoset)
#18.Define a function that returns the first n Fibonacci numbers as a list using tuples.
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print('Fibonacci series:',fibonacci(5))
#19.Use a list and dictionary to count the frequency of each character in a given string.
def charfrequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
print(charfrequency("Sairam"))

#20.Write a function to clear all items from a set and verify it is empty.
def clearsetandcheck(s):
    s.clear()
    return not s

myset = {1, 5, 10}
print('Set is empty :',clearsetandcheck(myset))
#Advanced Questions-------------------
#21.Implement a function to reverse the keys and values of a dictionary and return a new dictionary.
def reversedictionary(d):
    reverseddict = dict((v, k) for k, v in d.items())
    return reverseddict

original = {'a': 10, 'b': 20, 'c': 30}
reverseddict = reversedictionary(original)
print('Reverse the key and values of a dictionary :',reverseddict)
#22.Write code to sort a list of tuples by the second element using sorted() and lambda functions.
data = [(5, 2), (1, 3), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print('Sorted list:',sorted_data)
