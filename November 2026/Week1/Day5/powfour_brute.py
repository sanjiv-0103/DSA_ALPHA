def isPowerOfFour(n):
    if n==1:
        return True
    if n<=0 or n%4!=0:
        return False
    return isPowerOfFour(n//4)