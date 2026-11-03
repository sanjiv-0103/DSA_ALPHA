def intersection(a,b):
    result=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and a[i] not in result: #match checking
                result=result+[a[i]] #add to result
    return result