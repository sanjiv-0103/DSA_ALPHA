def running_sum(arr):
    result=[0]*len(arr)
    total=0
    for i in range(len(arr)):
        total+=arr[i]
        result[i]=total
    return result