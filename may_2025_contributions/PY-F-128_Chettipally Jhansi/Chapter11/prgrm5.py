import re
text = "Contact us at support@example.com or admin@site.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)
