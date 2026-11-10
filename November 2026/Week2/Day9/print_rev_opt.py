def print_reverse(head):
    if not head:
        return
    print_reverse(head.next)
    print(head.val,end=" ")