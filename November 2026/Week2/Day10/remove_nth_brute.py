def remove(head,n):
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    if n==count:
        return head.next
    curr=head
    for i in range(count-n-1):
        curr=curr.next
    curr.next=curr.next.next
    return head