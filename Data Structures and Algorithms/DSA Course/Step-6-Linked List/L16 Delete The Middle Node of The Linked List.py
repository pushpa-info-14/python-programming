from Leetcode.Common.ListNode import ListNode


def delete_mid(head: ListNode):
    if head is None or head.next is None:
        return None
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    target = n // 2
    cur = head
    while cur:
        target -= 1
        if target == 0:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head


def delete_mid2(head: ListNode):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next

    return head


l = ListNode.create([1, 2, 3, 4, 5])
l = delete_mid(l)
l.print()

l = ListNode.create([1, 2, 3, 4, 5])
l = delete_mid2(l)
l.print()
