"""Input three numbers and print True if they are in strictly increasing order (e.g., 2 < 5 < 9)."""
def main():
    """Check if three input numbers are strictly increasing."""
    #nums = []
    a,b,c = map(int, input("Enter three integers separated by space: ").split())

    # Check strictly increasing
    if a < b < c:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
