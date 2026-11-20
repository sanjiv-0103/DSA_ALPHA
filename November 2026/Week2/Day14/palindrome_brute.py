def isPalindrome(head):
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    left=head
    for i in range(count//2):
        right=head
        for j in range(count-i-1):
            right=right.next
        if left.val!=right.val:
            return False
        left=left.next
    return True
