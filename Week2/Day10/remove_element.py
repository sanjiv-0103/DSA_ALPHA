def remove_element(arr,val):
    write=0
    for read in range(len(arr)):
        if arr[read]!=val:
            arr[write]=arr[read]
            write+=1
    return write
arr=[3,2,2,3]
val=3
k=remove_element(arr,val)
print(k)
print(arr[:k])