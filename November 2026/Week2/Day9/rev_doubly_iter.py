def reverseDLL(head):
    curr=head
    newHead=None
    while curr:
        newHead=curr
        curr.prev,curr.next=curr.next,curr.prev
        curr=curr.prev
    return newHead