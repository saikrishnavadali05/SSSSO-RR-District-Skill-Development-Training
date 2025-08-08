'''Question 12:
decomposition / functions
Write a function square(n) that returns n*n and call it for numbers 1–5, printing each result.
'''
#solution
def square(n): #defining a function named square 
    return n*n #returns square of the paramater that is passed
for i in range(1,6): # for squaring numbers from 1 to 5
    print(square(i)) #calling the function and printing the output