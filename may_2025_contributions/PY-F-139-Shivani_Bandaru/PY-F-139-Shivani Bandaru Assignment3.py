chapter 8
Basic
1.number_list = list(range(1, 11))
print("List of numbers from 1 to 10:", number_list)

2.fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("The third fruit is:", fruits[2])

3.def add_numbers(a, b):
    return a + b
sum_result = add_numbers(5, 7)
print("The sum of 5 and 7 is:", sum_result)

Intermediate
 4(11).def get_even_numbers():
    return [x for x in range(1, 51) if x % 2 == 0]
even_numbers = get_even_numbers()
print("Even numbers from 1 to 50:", even_numbers)

5(12).squares_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of squares from 1 to 5:", squares_dict)

6(13).int_tuple = (3, 5, 7, 2, 8)  # Example tuple
tuple_sum = sum(int_tuple)
print("Sum of elements in the tuple:", tuple_sum)

advanced
7(21).def reverse_dict(original_dict):
    return {value: key for key, value in original_dict.items()}
sample_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dict(sample_dict)
print("Reversed dictionary:", reversed_dict)

8(22).tuple_list = [(1, 4), (3, 1), (5, 2), (2, 3)]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print("List of tuples sorted by second element:", sorted_list)

9(23).student = {
    "name": "Alice",
    "subjects": {
        "Math": 85,
        "Science": 92,
        "English": 78
    }
}
scores = student["subjects"].values()
average_score = sum(scores) / len(scores)
print(f"{student['name']}'s average score:", average_score)

10(24).def find_common_elements(list1, list2):
    return sorted(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = find_common_elements(list1, list2)
print("Common elements:", common)

