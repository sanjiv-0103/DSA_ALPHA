def min_add(s):
    count=0 
    add=0
    for ch in s:
        if ch=="(":
            count+=1
        else:
            if count>0:
                count-=1
            else:
                add+=1
    return add+count