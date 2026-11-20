def oddEvenList(head):
    if not head:
        return None
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    newHead=None
    tail=None
    for start in (0,1):
        for pos in range(start,count,2):
            curr=head
            for i in range(pos):
                curr=curr.next
            if not newHead:
                newHead=curr
            else:
                tail.next=curr
            tail=curr
    tail.next=None
    return newHead