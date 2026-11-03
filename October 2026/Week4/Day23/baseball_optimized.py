def baseball_game(ops):
    stack=[]
    total=0
    for op in ops:
        if op=="C":
            removed=stack.pop()
            total-=removed
        elif op=="D":
            value=stack[-1]*2
            stack.append(value)
            total+=value
        elif op=="+":
            value=stack[-1]+stack[-2]
            stack.append(value)
            total+=value
        else:
            value=int(op)
            stack.append(value)
            total+=value
    return total