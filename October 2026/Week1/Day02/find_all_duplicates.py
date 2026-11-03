def find_duplicates(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]: #comparing each element with the rest of the elements in the array
                if arr[i] not in result: #this ensures that we only add the duplicate once to the result list
                    result.append(arr[i]) #push to the reult list
    return result