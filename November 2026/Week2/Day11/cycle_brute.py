def cycle(head):
    curr=head
    for i in range(10001):
        if not curr:
            return False
        curr=curr.next
    return True