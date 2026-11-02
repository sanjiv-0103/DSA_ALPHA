def minCostClimbingStairs(cost):
    n=len(cost)
    dict={}
    def solve(i):
        if i>=n:
            return 0
        if i in dict:
            return dict[i]
        one=solve(i+1)
        two=solve(i+2)
        dict[i]=cost[i]+min(one,two)
        return dict[i]
    return min(solve(0),solve(1))