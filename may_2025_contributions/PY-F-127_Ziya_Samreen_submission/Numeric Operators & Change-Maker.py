amount = int(input("Enter an amount less than 100: "))
fifty_notes = amount // 50
ten_coins = (amount % 50) // 10
print(f"₹50 notes: {fifty_notes}, ₹10 coins: {ten_coins}")