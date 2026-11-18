def mergeDLL(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val<=list2.val:
        list1.next=mergeDLL(list1.next,list2)
        if list1.next:
            list1.next.prev=list1
        list1.prev=None
        return list1
    list2.next=mergeDLL(list1,list2.next)
    if list2.next:
        list2.next.prev=list2
    list2.prev=None
    return list2
