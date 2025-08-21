import re

sample_text = "Python3 is Amazing! It has 100s of libraries."
cleaned = re.sub(r'[^\w\s]', '', sample_text)   # Remove punctuation
cleaned = re.sub(r'\d+', '', cleaned)           # Remove digits
cleaned = cleaned.lower()                       # Convert to lowercase

print("Cleaned Text:", cleaned)

#Output:
# Cleaned Text: python is amazing it has s of libraries
