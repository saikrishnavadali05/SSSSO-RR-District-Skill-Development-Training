def square(n):
    """Return the square of n."""
    return n * n

def main():
    """Print squares of numbers 1 through 5."""
    for i in range(1, 6):
        print(f"square({i}) = {square(i)}")

if __name__ == "__main__":
    main()