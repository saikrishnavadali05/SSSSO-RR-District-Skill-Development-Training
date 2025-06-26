amount = int(input("Enter an amount less than 100: "))

fifty_notes = amount // 50
remaining = amount % 50

ten_notes = remaining // 10
remaining = remaining % 10

print("50 rupee notes:", fifty_notes)
print("10 rupee notes:", ten_notes)
print("Remaining rupees:", remaining)