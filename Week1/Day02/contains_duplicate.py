def contains_duplicate(arr):
    seen = set() #create an empty set
    for num in arr: #iterate through each element in the array
        if num in seen: #if the element is already in the set, it means we have found a duplicate
            return True
        seen.add(num) #if the element is not in the set, we add it to the set for future purposes
    return False