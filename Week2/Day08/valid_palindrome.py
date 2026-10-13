def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        while left<right and not isValid(s[left]):
            left+=1

        while left<right and not isValid(s[right]):
            right-=1
        a=toLower(s[left])
        b=toLower(s[right])
        if a!=b:
            return False
        left+=1
        right-=1
    return True

def isValid(ch):
    if 'a'<=ch<='z':
        return True
    if 'A'<=ch<='Z':
        return True
    if '0'<=ch<='9':
        return True
    return False

def toLower(ch):
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    i=0
    while i<26:
        if ch==upper[i]:
            return lower[i]
        i+=1
    return ch