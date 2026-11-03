def single_element(arr): #every pair of elements appears twice except for one element which appears only once
    result = 0
    for num in arr:
        result = result ^ num #XOR operation - logic: a^a = 0 and a^0 = a
    return result

#Rule Learnt : XOR Single Number:
#Pairs cancel ✅
#One single value remains ✅
#Two single values ❌
#A value appearing 3 times ❌