def find_disappeared(arr):
    n=len(arr)
    for i in range(n):
        value=arr[i]
        if value<0:
            value=-value
        index=value-1
        if arr[index]>0:
            arr[index]=-arr[index]
    count=0
    for i in range(n):
        if arr[i]>0:
            count+=1
    result=[0]*count
    j=0
    for i in range(n):
        if arr[i]>0:
            result[j]=i+1
            j+=1
    return result