def cycle(head):
    curr=head
    for i in range(10001):
        if not curr:
            return None
        curr=curr.next
    start=head
    while start:
        check=start.next
        for i in range(10000):
            if check==start:
                return start
            check=check.next
        start=start.next