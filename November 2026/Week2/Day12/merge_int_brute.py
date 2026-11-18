def merge(intervals):
    result=[item[:] for item in intervals]
    changed=True
    while changed:
        changed=False
        for i in range(len(result)):
            if changed:
                break
            for j in range(i+1,len(result)):
                a=result[i]
                b=result[j]
                if a[0]<=b[1] and b[0]<=a[1]:
                    result[i]=[min(a[0],b[0]),max(a[1],b[1])]
                    result.pop(j)
                    changed=True
                    break
    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
