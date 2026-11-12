def getnthfromend(head,n):
    if n<=0:
        return -1
    slow=head
    fast=head
    for i in range(n):
        if not fast:
            return -1
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    return slow.val