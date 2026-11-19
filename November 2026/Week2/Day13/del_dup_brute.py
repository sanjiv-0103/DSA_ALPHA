def del_dup(head):
    changed=True
    while changed:
        changed=False
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
                changed=True
                break
            curr=curr.next
    return head
