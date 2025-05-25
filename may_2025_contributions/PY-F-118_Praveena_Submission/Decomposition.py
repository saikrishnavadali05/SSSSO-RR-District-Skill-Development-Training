# Python Training 2025 - Decomposition of python code
# Description : Python program to understand the decoposition of code into blocks, functions or modules using simple calculator example
# Author : Praveena Kumbum
# Date : 20 May 2025
def Add(a,b):
    return a + b

def Subtract(a,b):
    return a - b

def Calculator():
    x = int(input("Please enetr the first value : "))
    y = int(input("Please enetr the second value : "))
    print("Add :", Add(x,y))
    print("Subtract :", Subtract(x,y))


if __name__ == "__main__":
    Calculator()