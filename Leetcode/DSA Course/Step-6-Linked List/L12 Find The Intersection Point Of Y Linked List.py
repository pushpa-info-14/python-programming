from Leetcode.Common.ListNode import ListNode


def find_intersection(head1: ListNode, head2: ListNode):
    mp = {}
    cur = head1
    while cur:
        mp[cur] = True
        cur = cur.next

    cur = head2
    while cur:
        if cur in mp:
            return cur
        cur = cur.next


def find_intersection2(head1: ListNode, head2: ListNode):
    t1, n1 = head1, 0
    t2, n2 = head2, 0
    while t1:
        n1 += 1
        t1 = t1.next
    while t2:
        n2 += 1
        t2 = t2.next

    t1 = head1
    t2 = head2
    if n1 < n2:
        for i in range(n2 - n1):
            t2 = t2.next
    else:
        for i in range(n1 - n2):
            t1 = t1.next

    while t1 != t2:
        t1 = t1.next
        t2 = t2.next
    return t1


def find_intersection3(head1: ListNode, head2: ListNode):
    t1 = head1
    t2 = head2
    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

        if t1 == t2: return t1

        if t1 is None: t1 = head2
        if t2 is None: t2 = head1


l1 = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
l2 = ListNode.create([7, 8])
l2.next.next = l1.next.next
l = find_intersection(l1, l2)
l.print()

l = find_intersection2(l1, l2)
l.print()

l = find_intersection3(l1, l2)
l.print()
