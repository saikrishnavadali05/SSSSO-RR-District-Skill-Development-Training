#Entering the inputs required
mode = input("Enter mode (encrypt/decrypt): ")
shift = int(input("Enter shift key: "))
message = input("Enter your message: ")
k = ""

#code for encrypting the message:
if mode == "encrypt":
    for i in message:
        if i.isupper():
            p = ord(i) - 65
            p += shift
            n = p % 26
            m = chr(65 + n)
        elif i.islower():
            p = ord(i) - 97
            p += shift
            n = p % 26
            m = chr(97 + n)
        else:
            m = i
        k += m

#code for decrypting the message:
elif mode == "decrypt":
    for i in message:
        if i.isupper():
            p = ord(i) - 65
            p = (p - shift) % 26
            m = chr(65 + p)
        elif i.islower():
            p = ord(i) - 97
            p = (p - shift) % 26
            m = chr(97 + p)
        else:
            m = i
        k += m
#Output of the code:
print("Result:", k)