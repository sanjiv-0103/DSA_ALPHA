def getnthterm(head,n):
    if n<=0:
        return -1
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    if n>count:
        return -1
    curr=head
    for i in range(count-n):
        curr=curr.next
    return curr.va