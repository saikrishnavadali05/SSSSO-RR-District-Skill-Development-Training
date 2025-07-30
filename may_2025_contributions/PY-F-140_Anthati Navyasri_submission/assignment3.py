List of a number from 1 to 9:
numbers = list(range(1, 11))
print("List of numbers from 1 to 10:", numbers)


Two numbers and returns their sum:
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print("The sum is:", result)


Five unique integers:
my_set = {10, 20, 30, 40, 50}
print("Length of the set:", len(my_set))


Maximum of three numbers:
def find_max(a, b, c):
    return max(a, b, c)
result = find_max(15, 22, 9)
print("The maximum number is:", result)


Sum of all elements:
numbers = (5, 10, 15, 20, 25)
total = sum(numbers)
print("Sum of all elements in the tuple:", total)


Fibonnacci numbers:
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    a, b = (0, 1)  
    for _ in range(2, n):
        a, b = (b, a + b)
        fib_list.append(b)
    return fib_list
print("First 10 Fibonacci numbers:", fibonacci(10))


Clear all items from a set:
def clear_and_check(my_set):
    my_set.clear()
    if len(my_set) == 0:
        print("The set is now empty.")
    else:
        print("The set is not empty.")
sample_set = {1, 2, 3, 4, 5}
clear_and_check(sample_set)


Reverse the keys and values of a dictionary:
def reverse_dict(original_dict):
    reversed_dict = {value: key for key, value in original_dict.items()}
    return reversed_dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_result = reverse_dict(my_dict)
print("Reversed dictionary:", reversed_result)


Single list using recursion:
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  
        else:
            flat_list.append(item)
    return flat_list
nested = [1, [2, [3, 4], 5], [6, 7], 8]
flattened = flatten_list(nested)
print("Flattened list:", flattened)



Generator function that yields tuples:
def my_enumerate(sequence):
    index = 0
    for item in sequence:
        yield (index, item)
        index += 1
my_list = ['a', 'b', 'c', 'd']
for idx, val in my_enumerate(my_list):
    print(f"Index: {idx}, Value: {val}")
    