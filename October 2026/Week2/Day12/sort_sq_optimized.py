def sorted_sq_optimized(arr):
    n=len(arr)
    result=[0]*n #creating a result arr of the same size as the input array
    left=0
    right=n-1
    pos=n-1
    while left<=right:
        left_square=arr[left]*arr[left] #taking sq of the left
        right_square=arr[right]*arr[right] #taking sq of the right
        if left_square>right_square: #if condition is true we will put the left sq in the result arr
            result[pos]=left_square #placing the larger square at the end
            left+=1 #increment pointer
        else:
            result[pos]=right_square #placing the larger square at the end
            right-=1
        pos-=1 
    return result