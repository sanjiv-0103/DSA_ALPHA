def miss_num(arr):
    n = len(arr)
    expected_sum = 0 #sum of all no.s from 0 to n
    actual_sum = 0 #sum of all no.s in the arr
    for i in range(n + 1): #claculate expectedsum
        expected_sum += i
    for num in arr:
        actual_sum += num #calculate actual sum
    return expected_sum - actual_sum    