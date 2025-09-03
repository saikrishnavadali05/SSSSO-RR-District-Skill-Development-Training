#30.Build a command-line Python tool that prints help messages and argument values using argparse.
import argparse

parser = argparse.ArgumentParser(description="Simple argparse example.")
parser.add_argument("--name", help="Enter your name")
parser.add_argument("--age", type=int, help="Enter your age")

args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Age: {args.age}")
#output: Name: <YourName>
#output: Age: <YourAge>
#output: Usage: python argparse_tool.py --name <YourName> --age <YourAge>
# Example usage: python argparse_tool.py --name John --age 30
'''Uses argparse to create a CLI with --name and --age arguments.
Automatically generates help messages.
Run example: python argparse_tool.py --name Harsha --age 23'''