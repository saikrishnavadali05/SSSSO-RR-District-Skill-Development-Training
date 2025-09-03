"""
Ask for an amount of rupees less than 100 and show how many ₹50 notes
and ₹10 coins are needed to make that amount.
"""

def main():
    """Calculate ₹50 notes and ₹10 coins needed for an amount < ₹100."""
    amount = int(input("Enter an amount in rupees (less than 100): "))
    notes_50 = amount // 50
    remaining = amount % 50
    coins_10 = remaining // 10
    print(f"₹50 notes: {notes_50}")
    print(f"₹10 coins: {coins_10}")

if __name__ == "__main__":
    main()
