import re
text = "My phone number is 98765 and ID is 123."
digits = re.findall(r'\d+', text)
print(digits)
