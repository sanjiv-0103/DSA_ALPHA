def daily_temp(temp):
    result=[0]*len(temp)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if temp[j]>temp[i]:
                result[i]=j-i
                break
    return result