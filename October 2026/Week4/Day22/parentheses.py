def valid(s):
    old="" #check if the str has changed after removing parentheses
    while old!=s: #until the str stops changing
        old=s #store the current str
        s=s.replace("()","") #remove valid parentheses
        s=s.replace("[]","")
        s=s.replace("{}","")
    return s=="" 