def pair_sum(arr, target): #this also brute force approach
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target: #checks if the sum of two elements is equal to target or not
                return [arr[i],arr[j]]

    return []