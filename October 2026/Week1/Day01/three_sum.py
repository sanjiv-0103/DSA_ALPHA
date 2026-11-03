def three_sum(arr):
    result = [] #creating an empty list to store
    for i in range(len(arr)):   #this loop will iterate from 0th index(i-th) to last
        for j in range(i + 1, len(arr)): #this loop will iterate from (i+1)th index to last
            for k in range(j + 1, len(arr)): #this loop will iterate from (j+1)th index to last
                if arr[i] + arr[j] + arr[k] == 0: #if condition is true then add the triplet to result
                    triplet = [arr[i], arr[j], arr[k]]  #triplet is created here
                    duplicate = False #check duplicate

                    for item in result: #
                        if set(item) == set(triplet): #if it is already present in the result or not
                            duplicate = True #if yes
                            break #breaks the loop
                    if not duplicate: #if not
                        result.append(triplet) #push the triplet to result
    return result