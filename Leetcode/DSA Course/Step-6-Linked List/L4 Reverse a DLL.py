from collections import deque

from Leetcode.Common.DoublyListNode import DoublyListNode


def createDoublyLinkedList(nums):
    n = len(nums)
    head = DoublyListNode(nums[0])
    prev = head
    for i in range(1, n):
        temp = DoublyListNode(nums[i], None, prev)
        prev.next = temp
        prev = temp
    return head


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


ls = createDoublyLinkedList([4, 2, 3, 1])
ls.print()
ls = reverse1(ls)
ls.print()

ls = createDoublyLinkedList([4, 2, 3, 1])
ls.print()
ls = reverse2(ls)
ls.print()
