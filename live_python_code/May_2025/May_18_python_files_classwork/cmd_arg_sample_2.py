import argparse

parser = argparse.ArgumentParser(description="Greet a user.")
parser.add_argument("name", help="Name of the user")
parser.add_argument("age", type=int, help="Age of the user")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Enable verbose output")

args = parser.parse_args()

greeting = f"Hello, {args.name}! You are {args.age}."
if args.verbose:
    greeting += " Nice to meet you!"

print(greeting)