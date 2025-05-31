amount = int(input("Enter amount less than 100: "))
fifties = amount // 50
tens = (amount % 50) // 10
print("₹50 notes:", fifties)
print("₹10 coins:", tens)