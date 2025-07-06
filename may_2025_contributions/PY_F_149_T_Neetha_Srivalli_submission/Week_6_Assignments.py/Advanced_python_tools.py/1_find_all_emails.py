import re        #Regular expression module

text = "Contact us at test@example.com or support@domain.org for help." 
                                 #Sample text containing email addresses
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text) 
                            #Finds all email addresses in the text using regex 

print(emails)   #Prints all the found email addresses

#Output:
#[']
