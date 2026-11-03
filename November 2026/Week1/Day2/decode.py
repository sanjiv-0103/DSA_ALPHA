def decode(s):
    n=len(s)
    def solve(i):
        if i==n:
            return 1
        if s[i]=='0':
            return 0
        ways=solve(i+1)
        if i+1<n:
            num=int(s[i:i+2])
            if 10<=num<=26:
                ways+=solve(i+2)
        return ways
    return solve(0)