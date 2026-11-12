def middle(head):
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    curr=head
    for i in range(count//2):
        curr=curr.next
    return curr