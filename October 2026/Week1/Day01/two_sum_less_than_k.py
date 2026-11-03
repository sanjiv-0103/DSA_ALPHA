def two_sum_less_than_k(arr, k):
    best=-1 #will store the best sum which is less than k
    for i in range(len(arr)):   #this loop will iterate from 0th index(i-th) to last
        for j in range(i+1, len(arr)): #this loop will iterate from (i+1)th index to last
            current=arr[i]+arr[j] #calculates sum of two elements
            if current<k and current>best:  #if condition is true then update best sum
                best=current
    return best