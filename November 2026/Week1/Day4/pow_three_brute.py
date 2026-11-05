def day4(n):
    if n==1:
        return True
    if n<=0 or n%3!=0:
        return False
    return day4(n//3)