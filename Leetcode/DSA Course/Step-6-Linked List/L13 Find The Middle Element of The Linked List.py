from Leetcode.Common.ListNode import ListNode


def find_mid(head: ListNode) -> ListNode:
    cnt = 0
    cur = head
    while cur:
        cnt += 1
        cur = cur.next

    target = (cnt // 2) + 1
    cur = head
    while cur:
        target -= 1
        if target == 0:
            break
        cur = cur.next
    return cur


def find_mid2(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


l = ListNode.create([1, 2, 3, 4, 5])
find_mid(l).print()
l = ListNode.create([1, 2, 3, 4, 5, 6])
find_mid(l).print()

l = ListNode.create([1, 2, 3, 4, 5])
find_mid2(l).print()
l = ListNode.create([1, 2, 3, 4, 5, 6])
find_mid2(l).print()
