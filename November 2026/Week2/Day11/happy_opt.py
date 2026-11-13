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
    slow=n
    fast=n
    while True:
        slow=digitsq(slow)
        fast=digitsq(digitsq(fast))
        if fast==1:
            return True
        if slow==fast:
            return False