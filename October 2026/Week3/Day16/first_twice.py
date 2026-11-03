def first_twice(s):
    seen={}
    for ch in s:
        if ch in seen:
            return ch
        else:
            seen[ch]=1
    return ""