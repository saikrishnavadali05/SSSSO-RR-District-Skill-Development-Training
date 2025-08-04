#15.Compare two strings for equality, ignoring case sensitivity
str1=input("Enter a string 1:")
str2=input("Enter a string 2:")
if str1.lower()==str2.lower():
    print("The two strings are equal")
else:
    print("The two strings are not equal")