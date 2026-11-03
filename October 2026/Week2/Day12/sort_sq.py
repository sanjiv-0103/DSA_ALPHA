def sort_sq(arr):
    result=[0]*len(arr)
    for i in range(len(arr)):
        result[i]=arr[i]*arr[i]
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if result[i]>result[j]:
                result[i],result[j]=result[j],result[i]
    return result