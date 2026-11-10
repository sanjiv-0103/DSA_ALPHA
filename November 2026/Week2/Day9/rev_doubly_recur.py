def reverseDLL(head):
    if not head:
        return None
    head.prev,head.next=head.next,head.prev
    if not head.prev:
        return head
    return reverseDLL(head.prev)