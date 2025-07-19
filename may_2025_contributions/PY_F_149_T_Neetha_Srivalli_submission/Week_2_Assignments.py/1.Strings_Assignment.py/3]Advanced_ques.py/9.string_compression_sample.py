def compress_string(s):   #defining the function to compress a string
    if not s: return ""    #Checks if the string is empty and returns an empty string if true
    result = ""    #Initializing the result string to store compressed characters
    count = 1   #Initializing the count of characters to 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  #checks if the current character is same as the previous one
            count += 1    #increments the count if they are same
        else:
            result += s[i - 1] + str(count)  #appends the character and its count to the result
            count = 1     #reset count for the next character
    result += s[-1] + str(count)  #appends the last character and its count to the result
    return result    #returns the compressed string

print(compress_string("aaabbbcccddd"))  #prints the compressed string
#Output:
# a3b3c3d3