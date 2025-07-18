# 20. Change-Maker
amount = int(input("Enter amount less than ₹100: "))
fifties = amount // 50
remainder = amount % 50
tens = remainder // 10
print("₹50 notes:", fifties)
print("₹10 coins:", tens)
# output: ₹50 notes: <number of ₹50 notes>
# output: ₹10 coins: <number of ₹10 coins>
# output example: If user enters 70, output will be "₹50 notes: 1" and "₹10 coins: 2"