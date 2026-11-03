def climbstairs(n): # climbStairs(n-1)+climbStairs(n-2)
    if n<=2:
        return n
    dp=[0]*(n+1) #creates a list with n+1 positions, initially filled with 0s
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]