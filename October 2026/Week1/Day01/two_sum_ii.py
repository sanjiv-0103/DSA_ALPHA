def two_sum_ii(arr, target):    #tired using brute force approach
    for i in range(len(arr)):   #this loop will iterate from 0th index(i-th) to last
        for j in range(i + 1, len(arr)): #this loop will iterate from (i+1)th index to last
            if arr[i] + arr[j] == target: #if condition is true then return the indices
                return [i + 1, j + 1] #returning the indices

    return [] #if no pair is found, return an empty list