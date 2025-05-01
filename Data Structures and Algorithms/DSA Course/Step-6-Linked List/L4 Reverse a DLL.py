from collections import deque

from Leetcode.Common.DoublyListNode import DoublyListNode


def reverse1(head: DoublyListNode):
    stack = deque()
    temp = head
    while temp:
        stack.append(temp.val)
        temp = temp.next

    temp = head
    while temp:
        temp.val = stack.pop()
        temp = temp.next

    return head


def reverse2(head: DoublyListNode):
    if head is None or head.next is None:
        return head
    cur = head
    prev = None
    while cur:
        prev = cur.prev
        cur.prev = cur.next
        cur.next = prev
        cur = cur.prev

    return prev.prev


ls = DoublyListNode.create([4, 2, 3, 1])
ls.print()
ls = reverse1(ls)
ls.print()

ls = DoublyListNode.create([4, 2, 3, 1])
ls.print()
ls = reverse2(ls)
ls.print()
