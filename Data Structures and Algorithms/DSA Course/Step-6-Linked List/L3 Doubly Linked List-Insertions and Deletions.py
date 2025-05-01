from typing import Optional

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


def deleteHead(head: DoublyListNode):
    if not head or not head.next:
        return None
    prev = head
    head = head.next
    head.prev = None
    prev.next = None

    return head


def deleteTail(head: DoublyListNode):
    if not head or not head.next:
        return None
    tail = head
    while tail.next:
        tail = tail.next

    prev = tail.prev
    tail.prev = None
    prev.next = None

    return head

def deleteKthElement(head: DoublyListNode, k:int):
    if not head:
        return head

    count = 0
    cur = head
    while cur:
        count += 1
        if count == k:
            break
        cur = cur.next

    prev = cur.prev
    next = cur.next
    if prev is None and next is None: # only one element.
        return None
    elif prev is None: # head
        return deleteHead(head)
    elif next is None: # tail
        return deleteTail(head)
    else:
        prev.next = next
        next.prev = prev

        cur.next = None
        cur.prev = None

    return head

def deleteNode(node: DoublyListNode):
    prev = node.prev
    next = node.next

    if next is None:
        prev.next = None
        node.prev = None
        return
    prev.next = next
    next.prev = prev
    node.next = None
    node.prev = None

def insertBeforeHead(head:DoublyListNode, val:int):
    temp = DoublyListNode(val, head, None)
    head.prev = temp
    return temp


def insertBeforeTail(head:Optional[DoublyListNode], val:int):
    if head is None:
        return DoublyListNode(val)
    if head.next is None:
        return insertBeforeHead(head, val)

    tail = head
    while tail.next:
        tail = tail.next

    prev= tail.prev
    temp = DoublyListNode(val, tail, prev)
    prev.next = temp
    tail.prev = temp
    return head

def insertBeforeKthElement(head:Optional[DoublyListNode], k:int, val):
    count = 0
    temp = head
    while temp:
        count += 1
        if count == k:
            break
        temp = temp.next
    prev = temp.prev
    if prev is None:
        return insertBeforeHead(head, val)
    else:
        new_node = DoublyListNode(val, temp, prev)
        prev.next = new_node
        temp.prev = new_node
        return head

def insertBeforeNode(node: DoublyListNode, val:int):
    prev = node.prev
    new_node = DoublyListNode(val, node, prev)
    prev.next = new_node
    node.prev = new_node

print("Q1: createDoublyLinkedList --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls.print()

print("Q2: deleteHead --------------------")
ls = deleteHead(ls)
ls.print()

print("Q3: deleteTail --------------------")
ls = deleteTail(ls)
ls.print()

print("Q4: deleteKthElement --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls = deleteKthElement(ls, 1)
ls.print()
ls = deleteKthElement(ls, 5)
ls.print()

print("Q5: deleteNode --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls.print()
deleteNode(ls.next.next)
ls.print()

print("Q6: insertBeforeHead --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls.print()
ls = insertBeforeHead(ls, 5)
ls.print()

print("Q7: insertBeforeTail --------------------")
ls = None
ls = insertBeforeTail(ls, 5)
ls = insertBeforeTail(ls, 2)
ls = insertBeforeTail(ls, 1)
ls.print()

print("Q8: insertBeforeKthElement --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls.print()
ls = insertBeforeKthElement(ls, 1,7)
ls.print()
ls = insertBeforeKthElement(ls, 7,8)
ls.print()

print("Q9: insertBeforeNode --------------------")
ls = createDoublyLinkedList([1, 2, 3, 4, 5, 6])
ls.print()
insertBeforeNode(ls.next.next, 7)
ls.print()