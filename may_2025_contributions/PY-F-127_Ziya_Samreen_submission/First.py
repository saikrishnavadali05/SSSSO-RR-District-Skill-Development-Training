def get_even_numbers():
    return [num for num in range(0, 11) if num % 2 == 0]

# Call the function
even_numbers = get_even_numbers()

# Print the 3rd last number
print("3rd last number:", even_numbers[-3])
