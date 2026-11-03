def max_avg(arr,k):
    tot=0
    for i in range(k):
        tot+=arr[i]
    best=tot
    for i in range(k,len(arr)):
        tot+=arr[i]
        tot-=arr[i-k]
        if tot>best:
            best=tot
    return best/k