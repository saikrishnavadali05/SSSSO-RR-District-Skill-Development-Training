#18.Extract the domain from an email address using slicing and split()
email=input("Enter email id : ")
split_email = email.split('@')  
domain = split_email[-1]        
print(domain)