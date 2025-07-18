'''Question 13:
indentation
Use a for loop to print a 5-row left-aligned triangle of * characters (1 on first row, 5 on last).
'''
#solution:
for i in range(6): #for loop to iterate over 5 rows 
    for j in range(i): #for loop to iterate over each element in each row and range is i since 1st row 1 element so on
        print("*",end="") #element on each row 
    print() # next line