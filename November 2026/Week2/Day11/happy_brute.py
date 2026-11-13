
def digitsq(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit*digit
        n//=10
    return total

def happy(n):
    if n<=0:
        return False
    while n!=1 and n!=4:
        n=digitsq(n)
    return n==1