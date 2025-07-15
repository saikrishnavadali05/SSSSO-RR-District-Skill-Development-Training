def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Only numbers allowed")
