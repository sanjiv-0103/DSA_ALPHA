def baseThree(n):
    if n<3:
        return str(n)
    return baseThree(n//3)+str(n%3)
