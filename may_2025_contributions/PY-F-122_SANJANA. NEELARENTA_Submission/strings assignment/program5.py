#Concatenate two strings using + operator and .format().

# Input two strings
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Concatenate using +
concatenated = string1 + string2

# Display result
print("Concatenated using '+':", concatenated)

# Concatenate using .format()
concatenated_format = "{}{}".format(string1, string2)

# Display result
print("Concatenated using '.format()':", concatenated_format)
