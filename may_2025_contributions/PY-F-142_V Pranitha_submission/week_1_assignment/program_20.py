'''question 20 
Ask for an amount of rupees less than 100 and show how many ₹50 notes and ₹10 coins are needed to make that amount (use // and %).

'''
#solution
amount=int(input("enter your amount"))
if amount<100:
    a=amount//50
    amount=amount%50
    b=amount//10
    amount=amount%10
    if amount<10 and amount!=0:
        print("remaning amount ",amount)


print("number of 50rs notes",a )
print("number of 10rs coins",b )