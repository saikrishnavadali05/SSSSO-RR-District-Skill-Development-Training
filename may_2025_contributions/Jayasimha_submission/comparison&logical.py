x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x > y > z:
    print("Numbers are in strictly decreasing order - False")
elif x < y < z:
    print("Numbers are in strictly increasing order - True")
else:
    print("Numbers are neither strictly increasing nor decreasing - False")

