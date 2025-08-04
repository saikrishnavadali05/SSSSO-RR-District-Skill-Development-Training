def convert_currency_static(amount, from_currency, to_currency):
    # Predefined exchange rates
    exchange_rates = {
        ('USD', 'EUR'): 0.92,
        ('EUR', 'USD'): 1.09,
        ('USD', 'INR'): 83.14,
        ('INR', 'USD'): 0.012,
    }

    key = (from_currency.upper(), to_currency.upper())
    if from_currency.upper() == to_currency.upper():
        return amount  # Same currency, no conversion needed

    if key in exchange_rates:
        rate = exchange_rates[key]
        return amount * rate
    else:
        print("❌ Exchange rate not found in static data.")
        return None


if __name__ == "__main__":
    print("💱 Static Currency Converter")

    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g. USD): ").strip()
        to_currency = input("To currency (e.g. EUR): ").strip()

        result = convert_currency_static(amount, from_currency, to_currency)

        if result is not None:
            print(f"\n✅ {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    except ValueError:
        print("❌ Invalid amount entered. Please enter a numeric value.")
