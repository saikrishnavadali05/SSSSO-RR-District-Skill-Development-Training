# Sum of numbers from 1 to n
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum is", sum)