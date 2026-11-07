def pascal(num_rows):
    triangle=[]
    for row in range(num_rows):
        curr=[1]*(row+1)
        for col in range(1,row):
            curr[col]=triangle[row-1][col-1]+triangle[row-1][col]
        triangle.append(curr)
    return triangle