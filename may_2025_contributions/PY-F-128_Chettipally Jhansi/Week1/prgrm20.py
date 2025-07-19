amount = int(input("Enter amount less than ₹100: "))

fifty_notes = amount // 50
remainder = amount % 50

ten_coins = remainder // 10

print("₹50 notes:", fifty_notes)
print("₹10 coins:", ten_coins)
