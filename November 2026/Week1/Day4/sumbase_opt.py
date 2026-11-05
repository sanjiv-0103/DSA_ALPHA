def sumBase(n,k):
    total=0
    while n>0:
        total+=n%k
        n//=k
    return total