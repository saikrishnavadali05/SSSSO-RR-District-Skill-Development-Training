amount = int(input("Enter rupees (<100): "))   #defines amoount to give input
fifties = amount // 50          #calculates the no.of 50's in the amount
remainder = amount % 50         #calculates the remainder after dividing by 50
tens = remainder // 10          #calculates the no.of 10's in the remainder
print("No.of fifties: ", fifties)
print("No.of tens: ", tens)
#Output:
#Enter rupees (<100): 90
#No.of fifties: 1
#No.of tens: 4