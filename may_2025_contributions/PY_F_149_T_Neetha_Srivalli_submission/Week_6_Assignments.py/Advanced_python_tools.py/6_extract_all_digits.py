import re    #Regular expression module

text = "Order #1234, shipped in 5 days on 2023-07-02."  #Sample text containing digits
digits = re.findall(r'\d+', text)    #Finds all sequences of digits in the text using reges

print(digits)    #Prints all the found sequences of digits

#Output:
#['1234', '5', '2023', '07', '02']
