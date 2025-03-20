from Leetcode.Common.ListNode import ListNode


def removeNthNode(head: ListNode, n: int):
    cnt = 0
    cur = head
    while cur:
        cnt += 1
        cur = cur.next

    if cnt == n:
        return head.next

    target = cnt - n
    cur = head
    while cur:
        target -= 1
        if target == 0:
            break
        cur = cur.next

    cur.next = cur.next.next
    return head


def removeNthNode2(head: ListNode, n: int):
    fast = head
    for i in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head


ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = removeNthNode(ll, 5)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = removeNthNode(ll, 6)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = removeNthNode2(ll, 5)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = removeNthNode2(ll, 6)
ll.print()
