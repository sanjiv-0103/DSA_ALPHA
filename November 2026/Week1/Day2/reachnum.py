def reachnum(target):
    if target<0:
        target=-target
    total=0
    moves=0
    while total<target or (total-target)%2!=0:
        moves+=1
        total+=moves
    return moves