def fib(n):
    dict={}
    def solve(num):
        if num<=1:
            return num
        if num in dict:
            return dict[num]
        dict[num]=solve(num-1)+solve(num-2)
        return dict[num]
    return solve(n)
print(fib(5))