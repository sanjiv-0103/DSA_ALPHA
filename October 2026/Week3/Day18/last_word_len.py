def last_word_length(s):
    count=0
    i=len(s)-1 #start from the last index of the str
    while i>=0 and s[i]==" ": 
        i-=1 #move to the prev char
    while i>=0 and s[i]!=" ": #count the len of the last word
        count+=1
        i-=1 #move to the prev char
    return count