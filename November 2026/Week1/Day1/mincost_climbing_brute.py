def minCostClimbingStairs(cost):
    n=len(cost)
    def solve(idx):
        if idx>=n:
            return 0
        one=solve(idx+1)
        two=solve(idx+2)
        return cost[idx]+min(one,two)
    return min(solve(0),solve(1))