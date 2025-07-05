chapter 5 strings

basic:

1.input_string = input("Enter a string: ")
if len(input_string) > 0:
    first_char = input_string[0]
    last_char = input_string[-1]
    print("First character:", first_char)
    print("Last character:", last_char)
else:
    print("The string is empty.")

2(3).input_string = input("Enter a string: ")
length = len(input_string)
print("The length of the input string is:", length)

3(10).name = input("Enter your name: ")
greeting = "Hello, {}! Welcome!".format(name)
print(greeting)

intermediate:

4(11).def reverse_string(s):
    return s[::-1]
input_str = "hello"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)

5(12).def is_only_digits(s):
    return s.isdigit()
input_str = "123456"
if is_only_digits(input_str):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

6(13).def replace_spaces_with_dashes(s):
    return s.replace(' ', '-')
input_str = "Hello World"
output_str = replace_spaces_with_dashes(input_str)
print(output_str)

advanced:

7(21).def custom_format(template, *args):
    return template.format(*args)
template = "Hello {0}, your balance is {1:.2f}."
formatted_str = custom_format(template, "Alice", 1234.567)
print(formatted_str)

8(22).def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return None  
    return max(words, key=len)
sentence = "I am learning Python programming language"
longest_word = find_longest_word(sentence)
print("Longest word:", longest_word)

9(23).def replace_spaces_with_dashes(s):
    return s.replace(' ', '-')
input_str = "Hello World"
output_str = replace_spaces_with_dashes(input_str)
print(output_str)

10(24).def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return None  
    return max(words, key=len)
sentence = "I am learning Python programming language"
longest_word = find_longest_word(sentence)
print("Longest word:", longest_word)

chapter 6 escape sequences
basic:
1.print("Hello,\nWelcome to Python programming!")

2.print("Name\t\tAge\tCity")
print("Alice\t\t25\tNew York")
print("Bob\t\t30\tLos Angeles")
print("Charlie\t\t22\tChicago")

3.print("This is a backslash: \\")

4.print('It\'s a beautiful day!')

intermediate:

5(11).print("Name\t\tAge\tCity\n")  
print("Alice\t\t25\tNew York")
print("Bob\t\t30\tLos Angeles")
print("Charlie\t\t22\tChicago")

6(12).file_path = "C:\\Users\\Shivani\\Documents\\Project\\file.txt"
escaped_path = file_path.replace("\\", "\\\\")
print("Original Path:", file_path)
print("Escaped Path: ", escaped_path)

7(13).import time
print("Loading...", end="\r")
time.sleep(2)
print("Complete!  ")

advanced:

8(21).user_input = input("Enter a string (use \\n for newline): ")
modified_string = user_input.replace("\\n", " ")
print("Modified string:", modified_string)

9(22).def print_with_line_numbers(multiline_string):
    lines = multiline_string.split('\n')  
    for i, line in enumerate(lines, start=1):
        print(f"Line {i}:\t{line}")
text = """This is line one.
This is line two.
This is line three."""
print_with_line_numbers(text)

10(23).import time
import datetime
try:
    while True: 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="", flush=True)
         time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")

chapter7 control structures
basic:

1.num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

2.num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The largest number is:", num1)
else:
    print("The largest number is:", num2)

3.num = 1
while num <= 10:
    print(num)
    num += 1  # Increment the number by 1

intermediate:

4(11).num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

5(12).print("Prime numbers between 1 and 100 are:")
for num in range(2, 101):  
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

6(13).num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10           
    sum_of_digits += digit     
    num = num // 10            
print("Sum of digits:", sum_of_digits)

7(14).num = int(input("Enter a number: "))
reversed_num = 0
original_num = num
num = abs(num)
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original_num < 0:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)

advanced:

8(21).print("Armstrong numbers between 100 and 999 are:")
for hundreds in range(1, 10):  
    for tens in range(0, 10):  
        for units in range(0, 10):  
            number = 100 * hundreds + 10 * tens + units
            sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (units ** 3)
             if number == sum_of_cubes:
                print(number)

9(22).num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator. Please enter one of +, -, *, /.")

10(23).num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator. Please enter one of +, -, *, /.")

