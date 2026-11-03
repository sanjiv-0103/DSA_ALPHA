def permutation_in_string(s1,s2):
    k=len(s1) #length of the first string
    for i in range(len(s2)-k+1): #iterate through all possible substrings of length k in s2
        part=s2[i:i+k] #extract substring of length k
        count1={} #count characters in s1
        count2={} #count characters in the current substring of s2
        for ch in s1:
            if ch in count1:
                count1[ch]+=1 #count occurrences of each char in s1
            else:
                count1[ch]=1 #initialize count for new char
        for ch in part:
            if ch in count2:
                count2[ch]+=1
            else:
                count2[ch]=1
        if count1==count2:
            return True
    return False