def countways(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return countways(n-1)+countways(n-2)+countways(n-3)