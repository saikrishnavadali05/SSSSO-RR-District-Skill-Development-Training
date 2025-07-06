def is_rotation(s1, s2):    #Function to check if s2 is a rotation of s1
    return len(s1) == len(s2) and s2 in (s1 + s1)  
    #Function to check if s2 is a rotation of s1

print(is_rotation("abc", "cab"))  #prints true if 'cab' is a rotation of 'abc'
print(is_rotation("abc", "acb"))  #prints true if 'acb' is a rotation of 'abc'
#Output:
# True
# false