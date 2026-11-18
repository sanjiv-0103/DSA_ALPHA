def mergeDLL(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val<=list2.val:
        head=list1
        list1=list1.next
    else:
        head=list2
        list2=list2.next
    head.prev=None
    tail=head
    while list1 and list2:
        if list1.val<=list2.val:
            node=list1
            list1=list1.next
        else:
            node=list2
            list2=list2.next
        tail.next=node
        node.prev=tail
        tail=node
    rest=list1 if list1 else list2
    if rest:
        tail.next=rest
        rest.prev=tail
    return head