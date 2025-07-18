amount = int(input("Enter the amount less than 100: "))

if amount >= 100:
    print("Amount should be less than ₹100")
else:
    fifty_notes = amount // 50             
    remainder = amount % 50                
    ten_coins = remainder // 10           

    print("Required ₹50 notes and ₹10 coins to make ₹", amount)
    print("₹50 notes:", fifty_notes)
    print("₹10 coins:", ten_coins)
