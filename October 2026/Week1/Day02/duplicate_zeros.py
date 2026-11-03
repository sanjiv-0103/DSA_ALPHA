def duplicate_zeros(arr):
    result=[]
    for i in arr:
        if len(result)==len(arr): #if the result[] has the same length as the arr
            break #break the loop
        result.append(i) #if not, push
        if i==0 and len(result)<len(arr):  #if curr is 0 and the result[] has not reached the len of arr
            result.append(0) #we push another 0
    for i in range(len(arr)): #take the result back to the og arr
        arr[i]=result[i] #copy each element from result to arr
    return arr  