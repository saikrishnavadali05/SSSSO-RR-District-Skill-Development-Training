#16.Split a string on a comma and print each element
text = input("Enter a string with commas : ")
elements = text.split(',')
for element in elements:
    print(element.strip())