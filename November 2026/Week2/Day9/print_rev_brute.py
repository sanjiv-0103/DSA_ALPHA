def print_reverse(head):
    n=0
    curr=head
    while curr:
        n+=1
        curr=curr.next
    for pos in range(n-1,-1,-1):
        curr=head
        for i in range(pos):
            curr=curr.next
        print(curr.val,end=" ")