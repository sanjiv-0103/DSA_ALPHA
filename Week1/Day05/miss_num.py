def miss_num(nums):
    count={} #
    for num in nums:
        count[num]=count.get(num,0)+1 #counts the freq of each num in the input list nums and stores it
    for num in count:
        if count[num]>len(nums) // 2:
            return num
    return -1