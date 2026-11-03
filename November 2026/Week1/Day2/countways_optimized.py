def countways(n):
    if n<=2:
        return 1 if n<=1 else 2
    prev1,prev2,prev3=2,1,1
    for i in range(3,n+1):
        curr=prev1+prev2+prev3
        prev3=prev2
        prev2=prev1
        prev1=curr
    return prev1