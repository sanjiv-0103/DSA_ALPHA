def set_mismatch(arr):
    n = len(arr)
    duplicate=0
    missing=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                duplicate=arr[i]
    for num in range(1,n+1):
        found=False
        for i in range(n):
            if arr[i]==num:
                found=True
                break
        if found==False:
            missing=num
    return [duplicate,missing]