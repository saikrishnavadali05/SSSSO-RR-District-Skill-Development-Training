bool1 = input("Enter first Boolean values: ")
bool2 = input("Enter second Boolean values: ")
bool1 = bool1 == "True"
bool2 = bool2 == "True"

print(bool1 and bool2, "AND:")
print(bool1 or bool2, "OR:")
print(not bool1, "NOT first:")
print(not bool2, "NOT second:")