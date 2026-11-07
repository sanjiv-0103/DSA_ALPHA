def printrow(rowIndex):
    def value(row,col):
        if col==0 or col==row:
            return 1
        return value(row-1,col-1)+value(row-1,col)
    result=[]
    for col in range(rowIndex+1):
        result.append(value(rowIndex,col))
    return result