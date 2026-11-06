def baseFour(n):
    if n==0:
        return "0"
    digits=[]
    while n>0: #extracting digitis to base 4
        digits.append(str(n%4))
        n//=4
        
    left,right=0,len(digits)-1 #reversing the digits
    while left<right:
        digits[left],digits[right]=digits[right],digits[left]
        left+=1
        right-=1
    return "".join(digits)