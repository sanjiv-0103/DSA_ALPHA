def pascal(num_rows):
    def value(row,col):
        if col==0 or col==row:
            return 1
        return value(row-1,col-1)+value(row-1,col)
    triangle=[]
    for row in range(num_rows):
        curr=[]
        for col in range(row+1):
            curr.append(value(row,col))
        triangle.append(curr)
    return triangle