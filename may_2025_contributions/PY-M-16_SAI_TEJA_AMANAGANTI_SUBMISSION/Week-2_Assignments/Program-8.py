#8.Count the number of occurrences of a character in a string
sw = input("Enter a string: ")
character= input("Enter the character whose count is required: ")
if sw:
    if character:
        print("Count of occurences of character in the string:",sw.count(character))
    else:
        print("Character not given")
else:
    print("String not given")