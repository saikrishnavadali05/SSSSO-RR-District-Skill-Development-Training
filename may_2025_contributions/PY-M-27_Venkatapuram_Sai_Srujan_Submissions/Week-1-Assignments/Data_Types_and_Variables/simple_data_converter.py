#22. Simulate a simple data type converter where the user selects a type (int, float, etc.) and provides a value.

# Get user input for target type
target_type = input("Enter the type to convert to (int, float, str): ").strip().lower()

# Get the value to convert
value = input("Enter the value to convert: ")

# Try conversion based on selected type
try:
    if target_type == "int":
        converted = int(value)
    elif target_type == "float":
        converted = float(value)
    elif target_type == "str":
        converted = str(value)
    else:
        print("Unsupported type selected.")
        converted = None

    if converted is not None:
        print("Converted Value:", converted)
        print("Type:", type(converted).__name__)
except ValueError:
    print("Conversion failed: Invalid input for the selected type.")


"""
Give the input as example:

Enter the type to convert to (int, float, str): float
Enter the value to convert: 42

"""