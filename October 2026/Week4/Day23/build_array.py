def build_array(target,n):
    result=[]
    j=0
    for num in range(1,n+1):
        result.append("Push")
        if num==target[j]:
            j+=1
        else:
            result.append("Pop")
        if j==len(target):
            break
    return result