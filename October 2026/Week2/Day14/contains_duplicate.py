def contains_duplicate(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and j-i<=k:
                return True

    return False