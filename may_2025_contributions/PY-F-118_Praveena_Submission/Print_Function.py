# Python Training 2025 - 
# Description : Python program to know the different ways of using print function
# Author : Praveena Kumbum
# Date : 20 May 2025
a = 10
b = "Shiva" 
print(f"My name is {b} and I am {a} years old.")

numbers = [1, 2, 3, 4, 5]
print(*numbers, sep=" | ", end=" <-- list complete\n")

with open("log.txt", "a") as log:
    print("Computation finished successfully.", file=log, flush=True)
print("Log written!")