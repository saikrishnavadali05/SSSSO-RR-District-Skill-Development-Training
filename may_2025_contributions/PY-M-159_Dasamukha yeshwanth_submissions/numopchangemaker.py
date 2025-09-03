amount = int(input("Enter an amount less than ₹100: "))
if 0 <= amount < 100:
    notes_50 = amount // 50
    remainder = amount % 50
    coins_10 = remainder // 10
    print(f"₹50 notes: {notes_50}")
    print(f"₹10 coins: {coins_10}")
else:
    print("Amount must be between ₹0 and ₹99.")
