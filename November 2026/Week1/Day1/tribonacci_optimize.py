def tribonacci(n):
    dict={}
    def solve(num):
        if num==0:
            return 0
        if num<=2:
            return 1
        if num in dict:
            return dict[num]
        dict[num]=solve(num-1)+solve(num-2)+solve(num-3)
        return dict[num]
    return solve(n)