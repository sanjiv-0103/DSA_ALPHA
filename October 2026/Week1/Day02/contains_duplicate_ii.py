def contains_duplicate_ii(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and j - i <= k: #this  ensures that the duplicate are within the specified distance k
                return True
    return False