# Simple Currency Converter

# Predefined exchange rates (example: 1 USD to others)
rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'INR': 83.0,
    'GBP': 0.75,
    'JPY': 110.0
}

# User input
amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, INR, GBP, JPY): ").upper()
to_currency = input("To currency (USD, EUR, INR, GBP, JPY): ").upper()

# Conversion
if from_currency in rates and to_currency in rates:
    converted = amount / rates[from_currency] * rates[to_currency]
    print(f"\n💱 {amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("❌ Invalid currency code.")