def missing_number(arr):
    n=len(arr)
    expected=0
    actual=0
    for i in range(n+1):
        expected+=i
    for i in range(n):
        actual+=arr[i]
    return expected-actual