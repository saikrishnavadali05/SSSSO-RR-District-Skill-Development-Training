def factorial(n):     #Function to calculate factorial of a number using recursion
    if n == 0 or n == 1:    #Return 1 if n is 0 or 1
        return 1
    return n * factorial(n - 1)    #Else multiply n with factorial of (n-1)
print(factorial(5))  
# Output: 120