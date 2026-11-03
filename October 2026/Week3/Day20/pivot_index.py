def pivot(arr):
    total=0
    for num in arr:
        total+=num
    left=0
    for i in range(len(arr)):
        right=total-left-arr[i]
        if left==right:
            return i
        left+=arr[i]
    return -1