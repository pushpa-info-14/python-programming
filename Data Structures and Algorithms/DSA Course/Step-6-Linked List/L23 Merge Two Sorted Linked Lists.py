from Leetcode.Common.ListNode import ListNode


def merge(head1: ListNode, head2: ListNode):
    dummy = ListNode(-1)

    temp = dummy
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp.next = temp1
            temp1 = temp1.next
        else:
            temp.next = temp2
            temp2 = temp2.next
        temp = temp.next

    if temp1:
        temp.next = temp1
    if temp2:
        temp.next = temp2

    return dummy.next


l1 = ListNode.create([2, 4, 8, 10])
l2 = ListNode.create([1, 3, 3, 6, 11, 14])
l = merge(l1, l2)
l.print()
