def intersect(a,b):
    result=[]
    used=[False]*len(b) #used list
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and used[j]==False: #match checking
                result=result+[a[i]] #add to result
                used[j]=True #mark that pos as used
                break
    return result