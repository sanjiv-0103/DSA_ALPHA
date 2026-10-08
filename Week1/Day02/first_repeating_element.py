def first_repeating(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]: #if found subsequent element is same as the current
                return arr[i] #return the first repeating element
    return -1 #if no repeating element is found