# range is a class of immutable iterable objects. 
# Their iteration behavior can be compared to lists: 
# you can't call next() directly on them; 
# you have to get an iterator by using iter.
# So no, range is not a generator.
# You may be thinking, "why didn't they make it directly iterable"? Well, ranges have some useful properties that wouldn't be possible that way:
# They are immutable, so they can be used as dictionary keys.
# They have the start, stop and step attributes (since Python 3.3), count and index methods and they support in, len and __getitem__ operations.
# You can iterate over the same range multiple times.

# range_variable = range(1, 21, 2)
# print(range_variable)
# print(range_variable.start)
# # 1
# print(range_variable.step)
# # 2
# print(range_variable.index(17))
# # 8
# print(range_variable.index(18))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 18 is not in range

# it = iter(range_variable)
# it
# <range_iterator object at 0x7f504a9be960>
# next(it)
# 1
# next(it)
# 3
# next(it)
# 5


# 25.6.2022

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# range(start, stop, step)
# range(1, 6, 2)
# for i in range(1, 5):
#     print(i, " ", i * i)
# print()

# for i in range(0, 25, 5):
#     print(i, " ", i * i)
# print()
# print(list(range(0, -10, -2)))
# print(tuple(range(0, -10, -2)))

# 3 values : start, stop, step

# data = ["a", 'b', 10, 3]
# print(data)
# print(data[1], data[1:-1])
# print(data[:2], ['c', 3 * 1])

# data = ["a", 'b', 10, 3, ['c', 'd', 'e']]
# print(data)

# def nested_list_demo():
#     data = ["a", 'b', 10, 3]
#     data[2:3] = [20, 30]  # change items
#     print(data) #['a', 'b', 20, 30, 3]
#     data[2:4] = []  # remove items
#     print(data) # ['a', 'b', 3]
#     data[2:2] = [15, 18, 22]  # insert items
#     print(data) # ['a', 'b', 15, 18, 22, 3]
#     print("length of data", len(data))
#     # nesting of lists
#     a = [10, 20, 12, 3]
#     b = [5, a, 30]
#     print(b)
#     print(b, b[1])
#     a.sort()
#     print(a)
#     b[1].append(25)
#     print(b)

# nested_list_demo()
# print()
# nested_list_demo()
# print()
# nested_list_demo()

# def add_two_numbers(number1, number2):
#     result = number1 + number2
#     return result

# def sub_two_numbers(number1, number2):
#     result = number2 - number1
#     return result

# addition_result = add_two_numbers(32, 42)
# subtraction_result = sub_two_numbers(10, 30)

# print(addition_result)
# print(subtraction_result)

# addition_result = add_two_numbers(100, 200)
# subtraction_result = sub_two_numbers(100, 200)

# print(addition_result)
# print(subtraction_result)

# def square(a):
#     '''
#     a (input) - some number
#     output - square of a
#     '''
#     return a * a

# print(square.__doc__)

# val = square(3)
# print(val)
# print(type(val))

# val = square
# print(val(100))

# output = square(int(input("give a number : ")))
# print(output)

# def square(number=10):
#     '''
#     the function square takes 10 as input (by default).
#     you can pass any value to this function
#     it will print the passed value.
#     '''
#     print(number)

# # can't be printed
# print(square.__doc__)

# string_variable = '''the function square takes 10 as input (by default).'''

# def sumodd(n = 5):
#  val = 0
#  index = 1
#  while (index <= n):
#  # if even we continue with next iteration
#    if (index % 2 == 0):
#      index += 1
#      continue
#  # if odd we add it
#    val += index
#    index += 1
#  return val

# def funNotImplemented(): 
#     pass

# print("sumodd is", sumodd(3))
# print("sumodd is", sumodd())
# funNotImplemented()

# def funckeyword(arg1, arg2='Multiple', arg3='Wishes'):
#     print("arg1=", arg1, "arg2=", arg2, "arg3=", arg3)

# # funckeyword(10)
# # funckeyword(arg1="value1")
  
# # funckeyword(10, arg2="Multiple")
# funckeyword(10, arg3="Wishes", arg2="MultipleWishes")
# # funckeyword(arg3="Hyderabad", arg1="value1")

# numbers = [10, 20, 30, 40]
# # numbers.append(50)
# # numbers.append(60, 70, 80, 90)
# # print(numbers)
# # numbers.extend([60, 70, 80, 90])
# # print(numbers)
# # pop_result = numbers.pop()
# # print(pop_result)
# # print(numbers)

# # print(numbers.__len__())
# # print(numbers.__doc__)

# print(dir(numbers))

t1 = (12, 5, 8)
l1 = [12, 5, 8]
print(t1[0])
print("index 1 in t1 is :", t1[1])
print(t1[2])

print(len(t1), max(t1), min(t1))

# t1[0] = 10 # illegal, due to immutability
# l1[0] = 10
# print(l1)
t2 = ("hello", 5)
t3 = (t1 + t2)
print(t3)
print(5 in t1)

for val in t1:
    print(val)

print(t1[1:])
# del t1
# print(t1)

print(t3)
# print(t1) throws error as we deleted t1
print(type(t2[0]))
print(type(t3))








