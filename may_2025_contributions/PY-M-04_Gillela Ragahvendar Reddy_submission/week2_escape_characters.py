# Basic--------------------
# 1. Write a Python program to print a string that includes a newline escape sequence \n.
print("Sairam!\nI am Raghu")

# 2. Demonstrate how to use the tab escape sequence \t to format output in columns.
print("Name\tID\tDesignation")
print("Raghu\t89076\tDeveloper")
print("Sai\t89077\tTester")
print("Ram\t89078\tBusinessAnalyst")

# 3. Show an example of printing a backslash \\ in a string.
print("Sairam Madam\\Sir!")

# 4. Write a program that uses the single quote escape sequence \' inside a string enclosed by single quotes.
print('Sairam!I am \'Raghu\'')

# 5. Write a program that uses the double quote escape sequence \" inside a string enclosed by double quotes.
print("Sairam!I am \"Raghu\"")

# 6. Print a string with a carriage return \r and explain its effect.
print("Sairam!I am Raghu\rWelcome")

# 7. Write a program demonstrating the backspace escape sequence \b by deleting characters from a printed string.
print("Sairam!I prayt\bo\b Swami")

# 8. Show how to print a string that contains both single and double quotes using escape sequences.
print('Sairam!\"Aren\'t you Raghu?\"')

# 9. Explain the effect of the alarm escape sequence \a and write a program that uses it.
print("Sairam!Good Morning\a")

# 10. Write a Python string that spans multiple lines using newline escape sequences.
print("Sairam!\nI am Raghu\nI love Swami")

# Intermediate--------------------
# 11. Create a program that prints a formatted table using tabs (\t) and newlines (\n).
print("Name\tID\tDesignation\n")
print("Raghu\t89076\tDeveloper\n")
print("Sai\t89077\tTester\n")
print("Ram\t89078\tBusinessAnalyst\n")

# 12. Write a program to replace all backslashes in a Windows file path string with double backslashes.
print("E:\\SSSSO-RR-District-Skill-Development-Training\\may_2025_contributions\\PY-F-112_Raghu_P_submission")

# 13. Explain and demonstrate how carriage return \r can be used to overwrite output on the same line.
print("Sairam! I am Raghu\rMorning")

# 14. Write a program that prints a string with a mix of quotes and escaped characters correctly.
print("Sairam Sir\\Madam!\'Your bhajan is Amazing. Let's have a bhajan session'")

# 15. Demonstrate the difference between printing a string with and without escape sequences using raw strings (prefix r).
print(r"Jai sai ram")
print(r"Jai\nsai\tram")

# 16. Write a program that prints a progress bar animation using carriage return \r.
import time
for i in range(11):
    print(f"\rProcessing... {i * 10}%", end="")
    time.sleep(0.3)
print("\nCompleted!")

# 17. Explain why the backspace escape sequence \b may not work as expected in some environments.
print("Aumm\b")
print("Aumm\b \b!")
print("Aumm\b\b\b!")

# 18. Create a string that includes an audible beep \a and test if the beep plays on your system.
print("Beep sound!\a")

# 19. Write a program that prints a dialogue between two people using newline and tab escape sequences for formatting.
print("Devotee A:\tSairam, how are you?\nDevotee B:\tI'm good, sairam! How about you?\n")
print("Devotee A:\tDoing well by swamis grace. Are you joining the buttermilk seva?\nDevotee B:\tSure sairam. When does it start?\n")
print("Devotee A:\tGreat! Let me share the seva coordinators contact number.You can get details from him sairam\nDevotee B:\tThank you sairam!")

# 20. Explain how escape sequences affect the length of a string. Write code to demonstrate your explanation.
s = "Sairam sir\\madam!\nHow are you?\tplease have swami's prasadam"
print("String contentt\b:",s)
print("\n it is Actual string length\r", len(s))

# Advanced------------------------------
# 21. Write a Python program that reads a string input from the user and replaces all newline escape sequences with a space.
str = input("Enter a string with \\n escape sequences: ")
replace_str = str.replace("\\n", " ")
print("Replaced string:", replace_str)

# 22. Create a function that takes a multiline string and prints each line prefixed with a line number using escape sequences.
def multiline(text):
    lines = text.split('\n')
    num= 1
    for line in lines:
        print("Line", num, ":", line)
        num += 1

sentences = """Sairam!
I am Raghu
I am a sai devotee"""
multiline(sentences)

# 23. Write a program that simulates a simple console clock updating every second using carriage return \r.
import time
for i in range(10): 
    print(f"\rClock: {time.strftime('%H:%M:%S')}", end="")
    time.sleep(1)
print("\nClock stopped")

# 24. Write code that demonstrates how to escape backslashes correctly in regular expressions within strings.
import re
pattern = "\\d+\\.\\d+"  
text = "The sai frame cost is 250.50 rupees"
match = re.search(pattern, text)
if match:
    print("Cost Matched:", match.group())

# 25. Explain and demonstrate how combining escape sequences can be used to format complex output (e.g., tables with indents and line breaks).
print("Name\t\tAge\tSamithi\n-------------------------------")
print("Sai\t\t30\tKodambakkam")
print("Ram\t\t25\tGuindy")
print("Raghu\t\t22\tWest Mmbalam")

# 26. Create a program that logs errors by printing error messages with a beep sound \a and formatting using tabs and newlines.
def log_error(msg):
    print(f"\a\tError: {msg}\n\tFile not found")
log_error("Invalid file format")

# 27. Write a program to clean a string of all escape characters and print the raw text only.
strn = "Sairam\\n I \\tam Raghu\\a"
removed = strn.replace("\\n", "").replace("\\t", "").replace("\\a", "")
print("Escape sequence replaced string:", removed)

# 28. Implement a text animation in the console using backspace \b to delete characters and rewrite them.
import time
print("Sairam!", end='', flush=True)
time.sleep(0.9)
print("\b\b\b\b\b\   \b\b\b\b\b", end='', flush=True)
time.sleep(0.9)
print("Sairam!", end='', flush=True)

# 29. Write a program that counts the number of escape sequences in a given string and outputs their types.
s = "Sairam\\\\Namaskaram\\nHow are you?\\t Please feel free\\nTake some prasadam\\b\\b\\bJaiSaiRam\\a aum"
print("Escape counts in the string :")
print("\\\\:", s.count("\\\\"))
print("\\n:", s.count("\\n"))
print("\\t:", s.count("\\t"))
print("\\b:", s.count("\\b"))
print("\\a:", s.count("\\a"))

# 30. Create a program that takes a file path input and converts it to a raw string format, escaping necessary characters.
path = input("Enter the file path :")
replacedpath = path.replace("\\", "\\\\")
print('r"' + replacedpath + '"')
