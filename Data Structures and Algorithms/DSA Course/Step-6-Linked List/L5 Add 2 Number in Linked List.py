from Leetcode.Common.ListNode import ListNode


def add(head1: ListNode, head2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    res = dummy
    temp1 = head1
    temp2 = head2
    carry = 0

    while temp1 and temp2:
        summation = temp1.val + temp2.val + carry
        carry = summation // 10
        rem = summation % 10
        dummy.next = ListNode(rem)

        temp1 = temp1.next
        temp2 = temp2.next
        dummy = dummy.next

    while temp1:
        summation = temp1.val + carry
        carry = summation // 10
        rem = summation % 10
        dummy.next = ListNode(rem)

        temp1 = temp1.next
        dummy = dummy.next

    while temp2:
        summation = temp2.val + carry
        carry = summation // 10
        rem = summation % 10
        dummy.next = ListNode(rem)

        temp2 = temp2.next
        dummy = dummy.next

    if carry:
        dummy.next = ListNode(carry)

    return res.next


ll1 = ListNode.create([3, 5])
ll2 = ListNode.create([4, 5, 9, 9])
ll = add(ll1, ll2)
ll.print()
