def single_num(arr):
    result = 0
    for num in arr:
        result = result ^ num # XOR operation - logic: a^a = 0 and a^0 = a
    return result