# Example 6: Using assert to catch bugs early
def calculate_area(radius):
  assert radius > 0, "Radius must be positive"
  return 3.14 * radius ** 2

print(calculate_area(5))

print(calculate_area(-5))
