'''Question 20:
numeric operators & change-maker
Ask for an amount of rupees less than 100 and show how many ₹50 notes and ₹10 coins are needed to make that amount (use // and %).
'''
#solution:
money=int(input("Enter the amount:")) #taking money as input
denomination={50:0,10:0} #dictonary for denominations setting 50rs andd 10rs values as 0 initially
if money>100: #if money less than 100 doesnt create denominations
    print("The amount must be less than 100 rs")
else: 
        denomination[50]=money//50 #storing denomination of 50 by diving the money by 50
        money=money % 50 #money is updated to the remaining money by modulo
        denomination[10]=money//10
        money=money % 10
        if money<10 and money !=0 : # for money less than 10 and not 0
              print(f"Remaining {money} cant be distributed in 50rs notes or 10rs")
print(denomination)