def insertion_sort(arr):     #Function to perform insertion sort on an array
    for i in range(1, len(arr)):  #Iterate through the array starting from the second element
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:   #While the current element is less than the previous elements
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr         #Return the sorted array

print(insertion_sort([5, 2, 9, 1, 5, 6]))

#Output: 
# [1, 2, 5, 5, 6, 9]