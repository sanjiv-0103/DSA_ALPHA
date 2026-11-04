def power_of_three(n):
    if n==1:
        return False
    if n<=0 or n%3!=0:
        return False
    return power_of_three(n//3)