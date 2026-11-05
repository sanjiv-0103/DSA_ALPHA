def baseThree(n):
    if n==0:
        return "0"
    digits=[]
    while n>0:
        digits.append(str(n%3))
        n//=3
    left,right=0,len(digits)-1
    while left<right:
        digits[left],digits[right]=digits[right],digits[left]
        left+=1
        right-=1
    return "".join(digits)