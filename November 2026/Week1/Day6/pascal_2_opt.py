def printrow(rowIndex):
    prev=[1]
    for row in range(1,rowIndex+1):
        curr=[1]*(row+1)
        for col in range(1,row):
            curr[col]=prev[col-1]+prev[col]
        prev=curr
    return prev