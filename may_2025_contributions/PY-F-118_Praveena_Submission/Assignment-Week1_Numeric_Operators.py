# Python Training 2025 - Numeric operators
# Description : Python program : Ask the user for two whole numbers and print their sum, difference, product, and quotient.
# Author : Praveena Kumbum
# Date : 21 May 2025
def Add(a,b):
    return a + b
def Subtract(a,b):
    return a - b
def Product(a,b):
    return a * b
def Divide(a,b):
    return a / b

def Calculator():
    x = int(input("Please enter the first number : "))
    y = int(input("Please enter the second number : "))
    print("Sum is : ", Add(x,y))
    print("Differnece is : ", Subtract(x,y))
    print("Product is : ", Product(x,y))
    print("Quotient is : ", Divide(x,y))

if __name__ == "__main__":
    Calculator()