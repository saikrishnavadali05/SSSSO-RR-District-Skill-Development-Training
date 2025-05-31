data_type = input("Enter data type (int, float, str, bool): ").strip()
value = input("Enter a value: ")

if data_type == "int":
    converted = int(value)
elif data_type == "float":
    converted = float(value)
elif data_type == "bool":
    converted = value.lower() in ("true", "1")
else:
    converted = value

print("Converted value:", converted, "| Type:", type(converted))