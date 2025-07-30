def log_io(func):
    def wrapper(*args, **kwargs):
        print(f"Input: {args}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_io
def reverse_string(s):
    return s[::-1]

reverse_string("hello")
#Output:
# Input: ('hello',)
# Output: olleh