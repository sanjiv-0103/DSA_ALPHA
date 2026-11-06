def basefour(n):
    if n<4:
        return str(n)
    return basefour(n//4)+str(n%4)
