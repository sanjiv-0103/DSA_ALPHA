def power_of_two(n):
    if n==1:
        return False
    if n<=0 or n%2!=0:
        return False
    return power_of_two(n//2)