from typing import Optional

from Leetcode.Common.ListNode import ListNode


def deleteHead(head: ListNode):
    if head is None: return head
    head = head.next  # This does not update the original head. You should assign the return value
    return head


def deleteTail(head: ListNode):
    if head is None: return None
    if head.next is None: return None

    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head


def deleteAtK(head: ListNode, k: int):
    if head is None: return None

    if k == 1:
        head = head.next
        return head

    count = 0
    cur = head
    while cur:
        count += 1
        if count == k - 1:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head


def deleteElement(head: ListNode, target: int):
    if head is None: return None

    if head.val == target:
        head = head.next
        return head

    cur = head
    prev = None
    while cur:
        if cur.val == target:
            prev.next = prev.next.next
            break
        prev = cur
        cur = cur.next
    return head


def insertAtHead(head: ListNode, val: int):
    return ListNode(val, head)


def insertLasAtTail(head: Optional[ListNode], val: int):
    if not head:
        return ListNode(val)

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = ListNode(val)
    return head


def insertAtK(head: Optional[ListNode], k: int, val: int):
    if not head:
        if k == 1:
            return ListNode(val)
        else:
            return head
    if k == 1:
        return ListNode(val, head)
    count = 0
    cur = head
    while cur:
        count += 1
        if count == k - 1:
            cur.next = ListNode(val, cur.next)
            break
        cur = cur.next
    return head


def insertBefore(head: Optional[ListNode], target: int, val: int):
    if not head:
        return head
    if head.val == target:
        return ListNode(val, head)

    cur = head
    while cur:
        if cur.next.val == target:
            cur.next = ListNode(val, cur.next)
            break
        cur = cur.next
    return head


print("Q1: deleteHead --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteHead(head)
head.print()

print("Q2: deleteTail --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteTail(head)
head.print()

print("Q3: deleteAtK --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteAtK(head, 3)
head.print()
head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteAtK(head, 2)
head.print()

print("Q4: deleteElement --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = deleteElement(head, 2)
head = deleteElement(head, 1)
head.print()

print("Q5: insertAtHead --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = insertAtHead(head, 25)
head.print()

print("Q6: insertLasAtTail --------------------")
head = None
head = insertLasAtTail(head, 25)
head = insertLasAtTail(head, 2)
head.print()

print("Q7: insertAtK --------------------")
head = None
head = insertAtK(head, 1, 25)
head.print()
head = ListNode(1, ListNode(2, ListNode(3)))
head = insertAtK(head, 3, 25)
head.print()

print("Q8: insertBefore --------------------")
head = ListNode(1, ListNode(2, ListNode(3)))
head = insertBefore(head, 3, 25)
head = insertBefore(head, 2, 27)
head.print()
