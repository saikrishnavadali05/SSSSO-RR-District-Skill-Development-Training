# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added, supporting the usual dict methordered_dicts. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

# Example : OrderDictionary1.py

# import time
# import os
# import sys
# import subprocess

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['c'] = 1
ordered_dict['b'] = 2
ordered_dict['a'] = 3
print(ordered_dict.items())
print("-----------------------------------")

dict = {}
dict['c'] = 1
dict['b'] = 2
dict['a'] = 3
print(dict.items())
#sample output:
# Output:

# odict_items([('c', 1), ('b', 2), ('a', 3)])
# dict_items([('c', 1), ('b', 2), ('a', 3)])

# Example : OrderDictionary2.py

# Key value Change: Even if the value of a certain key is changed, 
# the position of the key remains unchanged in an OrderedDict.

print("As a ordered dict : ")

from collections import OrderedDict
print("Before:")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

ordered_dict['c'] = 5
print(ordered_dict)

# # from collections import OrderedDict
# print("As a dict : ")
# dict = {}
# dict['a'] = 1
# dict['b'] = 2
# dict['c'] = 3
# dict['d'] = 4

# print(dict)

# dict['c'] = 5
# print(dict)


# Output:

# Before:
# a 1
# b 2
# c 3
# d 4

# After:
# a 1
# b 2
# c 5
# d 4


# Example : OrderDictionary3.py

# Deletion and Re-Insertion - Deleting and re-inserting the same key will push 
# it to the back as OrderedDict, 
# however, maintains the order of insertion.

from collections import OrderedDict

print("Before deleting:")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

print("\nAfter deleting:")
ordered_dict.pop('c')

print(ordered_dict)

print("\nAfter re-inserting:")
ordered_dict['c'] = 3

print(ordered_dict)

# Example : OrderDictionary4.py

import collections
dict1 = {}
dict1['a'] = 'A'
dict1['b'] = 'B'
dict1['c'] = 'C'

dict2 = {}
dict2['c'] = 'C'
dict2['b'] = 'B'
dict2['a'] = 'A'

print(dict1)
print(dict2)

print('Is dict1 same as dict2 ?', dict1 == dict2)

# ordered_dict1 = collections.OrderedDict()
# ordered_dict1['a'] = 'A'
# ordered_dict1['b'] = 'B'
# ordered_dict1['c'] = 'C'

# ordered_dict2 = collections.OrderedDict()
# ordered_dict2['c'] = 'C'
# ordered_dict2['b'] = 'B'
# ordered_dict2['a'] = 'A'

# print(ordered_dict1)
# print(ordered_dict2)


# print('Is ordered_dict1 same as ordered_dict2 ?', ordered_dict1 == ordered_dict2)

# Output:

# dict: True
# OrderedDict: False
# Example : OrderDictionary5.py

# import collections
# d = collections.OrderedDict(
# [('a', 'A'), ('b', 'B'), ('c', 'C')]
# )
# print('Before:')
# for k, v in d.items():
#     print(k, v)
# d.move_to_end('b')
# print('\nmove_to_end():')
# for k, v in d.items():
#     print(k, v)
# d.move_to_end('b', last=False)
# print('\nmove_to_end(last=False):')
# for k, v in d.items():
#     print(k, v)
# Output:

# Before:
# a A
# b B
# c C

# move_to_end():
# a A
# c C
# b B

# move_to_end(last=False):
# b B
# a A
# c C
# The only difference between dict() and OrderedDict() is that: OrderedDict preserves the order in which the keys are inserted.