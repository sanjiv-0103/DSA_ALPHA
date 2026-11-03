def remove_dup(arr):
    if len(arr)==0:
        return 0
    write=1 #index of next unique element should be placed
    for read in range(1,len(arr)):
        if arr[read]!=arr[read-1]:
            arr[write]=arr[read]
            write+=1
    return write
arr=[1,1,2,2,3]
k=remove_dup(arr)
print(k)
print(arr[:k])