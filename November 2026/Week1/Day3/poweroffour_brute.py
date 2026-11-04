def power_of_four(n):
    if n==1:
        return False
    if n<=0 or n%4!=0:
        return False
    return power_of_four(n//4)