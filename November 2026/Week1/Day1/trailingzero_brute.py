def trailingZeroes(n):
    fact=1
    for num in range(2,n+1):
        fact*=num
    count=0
    while fact%10==0:
        count+=1
        fact//=10
    return count