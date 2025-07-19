#Create an OrderedDict with three key-value pairs and print its keys in insertion order.

from collections import OrderedDict

# Create an OrderedDict with three key-value pairs
student_scores = OrderedDict()
student_scores["Alice"] = 90
student_scores["Bobby"] = 85
student_scores["Champ"] = 95

# Print the keys in insertion order
print("Keys in insertion order:")
for key in student_scores:
    print(key)
