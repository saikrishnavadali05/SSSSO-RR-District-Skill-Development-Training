'''question 13
Use a for loop to print a 5-row left-aligned triangle of * characters (1 on first row, 5 on last).

'''
#solution
def print_star_pattern(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        print()
        
print_star_pattern(5)


