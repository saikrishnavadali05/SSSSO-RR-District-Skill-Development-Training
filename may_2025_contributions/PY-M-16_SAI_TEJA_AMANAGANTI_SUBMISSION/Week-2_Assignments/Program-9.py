#9.substring is present in a given string
words = input("Enter the main string: ")
substr = input("Enter the substring to search for: ")
if substr in words:
    print("Substring is present in the main string")
else:
    print("Substring is not present in the main string")