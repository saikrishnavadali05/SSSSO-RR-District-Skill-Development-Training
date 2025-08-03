#5.Concatenate two strings using + operator and .format()
s1=input("Enter a string 1:")
s2=input("Enter a string 2:")
if s1 and s2:
    print("Concatenated two strings using + operator",s1+" "+s2)
    print("Concatenated two strings using .format()","{} {}".format(s1,s2))
else:
    print("Please enter valid strings")