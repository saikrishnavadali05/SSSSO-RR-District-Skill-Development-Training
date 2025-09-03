"""Read a temperature in C (float) and convert it to F using the formula F = C*9/5 + 32."""
def main():
    """Convert Celsius to Fahrenheit."""
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius}°C is {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
