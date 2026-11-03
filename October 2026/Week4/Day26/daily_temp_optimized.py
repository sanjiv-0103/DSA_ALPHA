def daily_temp(temp):
    result=[0]*len(temp)
    stack=[]
    for i in range(len(temp)):
        while len(stack)>0 and temp[i]>temp[stack[-1]]:
            old=stack.pop()
            result[old]=i-old
        stack.append(i)
    return result