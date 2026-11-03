def merge_intervals(arr):
    result=[]
    for inter in arr:
        merged=False
        for i in range(len(result)):
            if inter[0]<=result[i][1] and inter[1]>=result[i][0]:
                start=min(inter[0],result[i][0])
                end=max(inter[1],result[i][1])
                result[i]=[start,end]
                merged=True
                break
        if merged==False:
            result=result+[inter]
    return result