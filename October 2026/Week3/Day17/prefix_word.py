def prefix_word(sentence,search):
    words=sentence.split()
    for i in range(len(words)):
        word=words[i]
        if word[:len(search)]==search:
            return i+1
    return -1