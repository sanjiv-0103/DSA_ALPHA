def baseball_brute(ops):
    scores=[]
    for op in ops: #op-single operation & ops-operations 
        if op=="C":
            scores.pop()
        elif op=="D":
            scores.append(scores[-1]*2)
        elif op=="+":
            scores.append(scores[-1]+scores[-2])
        else:
            scores.append(int(op))
    total=0
    for score in scores:
        total+=score
    return total