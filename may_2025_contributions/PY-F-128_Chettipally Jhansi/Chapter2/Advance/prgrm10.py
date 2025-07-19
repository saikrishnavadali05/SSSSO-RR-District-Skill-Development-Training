import argparse

parser = argparse.ArgumentParser(description="A simple arithmetic CLI tool")
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")
parser.add_argument("--operation", choices=["add", "sub"], default="add", help="Operation to perform")

args = parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2
else:
    result = args.num1 - args.num2

print(f"Result: {result}")
