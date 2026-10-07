def sum(arr, target):
    for i in range(len(arr)):           #this loop will iterate from 0th index(i-th) to last 
        for j in range(i+1, len(arr)):  #this loop will iterate from (i+1)th index to last
            if arr[i]+arr[j]==target:   #comparing the sum with target
                return [i, j]           

    return []
