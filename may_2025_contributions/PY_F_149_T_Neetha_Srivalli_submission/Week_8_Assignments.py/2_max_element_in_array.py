def find_max(arr):   #Function to find the maximum element in  an array
    if not arr:    #If the array is empty, return None
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:    #If the current number is greater than max_val, update max_val
            max_val = num    #Update max_val with the current number
    return max_val  

# Example usage
print(find_max([10, 22, 3, 45, 7]))

#Output:
# 45