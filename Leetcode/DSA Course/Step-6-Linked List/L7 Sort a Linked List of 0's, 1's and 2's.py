from Leetcode.Common.ListNode import ListNode


def sortLinkedList1(head: ListNode):
    if head is None or head.next is None:
        return head
    count0 = 0
    count1 = 0
    count2 = 0

    cur = head
    while cur:
        if cur.val == 0:
            count0 += 1
        elif cur.val == 1:
            count1 += 1
        elif cur.val == 2:
            count2 += 1
        cur = cur.next

    cur = head
    while count0 > 0:
        cur.val = 0
        count0 -= 1
        cur = cur.next
    while count1 > 0:
        cur.val = 1
        count1 -= 1
        cur = cur.next
    while count2 > 0:
        cur.val = 2
        count2 -= 1
        cur = cur.next

    return head


def sortLinkedList2(head: ListNode):
    if head is None or head.next is None:
        return head

    zero_head = ListNode(-1)
    one_head = ListNode(-1)
    two_head = ListNode(-1)
    zero = zero_head
    one = one_head
    two = two_head

    cur = head
    while cur:
        if cur.val == 0:
            zero.next = cur
            zero = cur
        elif cur.val == 1:
            one.next = cur
            one = cur
        elif cur.val == 2:
            two.next = cur
            two = cur
        cur = cur.next

    zero.next = one_head.next if one_head.next else two_head.next
    one.next = two_head.next
    two.next = None

    return zero_head.next


ll = ListNode.create([1, 0, 1, 2, 0, 2, 1])
ll.print()
ll = sortLinkedList1(ll)
ll.print()

ll = ListNode.create([1, 0, 1, 2, 0, 2, 1])
ll.print()
ll = sortLinkedList2(ll)
ll.print()
