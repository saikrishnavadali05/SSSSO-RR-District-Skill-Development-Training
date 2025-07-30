# creating a function that prints my first name and last name
def firstname_lastname():
    First_name = "divyasree"
    last_name = "talari"
    print(First_name + " " + last_name)

# this function will print sum of two whole numbers, difference, product and quotient
def numeric_operator():
    a = int(input("Enter first whole number: "))
    b = int(input("Enter second whole number: "))
    sum_ = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("sum =", sum_)
    print("difference =", difference)
    print("product =", product)
    print("quotient =", quotient)

# Call the functions
firstname_lastname()
numeric_operator()