from Leetcode.Common.ListNode2 import ListNode2


def merge(head1: ListNode2, head2: ListNode2):
    dummy = ListNode2(-1)
    temp = dummy
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp.child = temp1
            temp1 = temp1.child
        else:
            temp.child = temp2
            temp2 = temp2.child
        temp = temp.child
        temp.next = None
    if temp1:
        temp.child = temp1
    if temp2:
        temp.child = temp2
    return dummy.child


def flatten(head: ListNode2):
    if head is None or head.next is None:
        return head
    return merge(head, flatten(head.next))


l1 = ListNode2.create([3])
l2 = ListNode2.create([2, 10])
l3 = ListNode2.create([1, 7, 11, 12])
l4 = ListNode2.create([4, 9])
l5 = ListNode2.create([5, 6, 8])
l = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l = flatten(l)
l.print()
