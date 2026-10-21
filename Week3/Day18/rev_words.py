def reverse_words(s):
    chars=list(s) #convert the string into a list of char
    start=0
    for i in range(len(chars)+1):
        if i==len(chars) or chars[i]==" ": #when reached the end of a word
            left=start
            right=i-1
            while left<right:
                chars[left],chars[right]=chars[right],chars[left] #swap the char
                left+=1
                right-=1
            start=i+1
    return "".join(chars)