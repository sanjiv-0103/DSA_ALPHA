def sumPascalRow(rowIndex):
    total=1
    for i in range(rowIndex):
        total*=2
    return total

#def sumPascalRow(rowIndex):
#    return 1<<rowIndex