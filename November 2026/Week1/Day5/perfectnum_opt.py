def perfectnum(num):
    if num<=1:
        return False
    total=1
    val=2
    while val*val<=num:
        if num%val==0:
            total+=val
            pair=num//val
            if pair!=val:
                total+=pair
        val+=1
    return total==num