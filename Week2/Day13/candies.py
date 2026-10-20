def greatestcandies(arr,extra):
    biggest=arr[0] #to find the biggest number
    for num in arr:
        if num>biggest:
            biggest=num
    result=[]
    for num in arr:
        if num+extra>=biggest:
            result=result+[True]
        else:
            result=result+[False]
    return result