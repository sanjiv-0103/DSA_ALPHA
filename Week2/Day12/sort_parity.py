def sort_parity(arr):
    result=[0]*len(arr) #creating a result arr of the same size as the input array
    even=0
    odd=1
    for num in arr:
        if num%2==0: #if the num is even
            result[even]=num
            even+=2 #move the even pointer to the next even pos
        else:
            result[odd]=num
            odd+=2 #move the odd pointer to the next odd pos
    return result