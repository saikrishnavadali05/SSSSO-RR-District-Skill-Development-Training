amount = int(input("Enter amount (less than 100): "))

if amount < 100:
    print("₹50 notes:", amount // 50)
    print("₹10 coins:", (amount % 50) // 10)
else:
    print("Amount should be less than 100")