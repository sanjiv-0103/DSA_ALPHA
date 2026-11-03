def long_prefix(words):
    if len(words)==0:
        return ""
    first=words[0]
    for i in range(len(first)):
        ch=first[i]
        for j in range(1,len(words)):
            if i>=len(words[j]) or words[j][i]!=ch:
                return first[:i]
    return first