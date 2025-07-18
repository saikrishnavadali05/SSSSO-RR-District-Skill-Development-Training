'''Question 5:
logical operators
Read two Boolean values (e.g., True/False) and print the results of and, or, and not on them.

'''
#solution
bool1=int(input()) #Input from user
bool2=int(input()) 
print("and :",bool1 & bool2) # bitwise and on operands 
print("or :",bool1|bool2) # bitwise or on operands
print("not on bool1:",not bool1 ) # not on first operand
print("not on bool2:",not bool2) #not on 2nd operand