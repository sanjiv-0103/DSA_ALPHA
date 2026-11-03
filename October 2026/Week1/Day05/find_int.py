def findSpecialInteger(arr):
    count={} #dict to store the count of each element
    for num in arr:
        count[num]=count.get(num,0)+1
        if count[num]>len(arr) // 4:
            return num