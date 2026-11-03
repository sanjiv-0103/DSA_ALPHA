def find_diff_char(a,b):
    result=0
    for ch in a: #ord() function returns the ACII value of the char
        result=result^ord(ch) #XOR operation - logic: a^a = 0 and a^0 = a
    for ch in b:
        result=result^ord(ch) 
    return chr(result)