def single_num_ii(arr):
    count={} #dict - to store the count of each element
    for num in arr:
        if num in count: #if the element is already present in the dict, increment its count
            count[num]+=1 #increment the count of the element
        else:
            count[num]=1 #add the element to the dict with a count of 1
    for num in count:
        if count[num]==1: #if the count is 1, return
            return num