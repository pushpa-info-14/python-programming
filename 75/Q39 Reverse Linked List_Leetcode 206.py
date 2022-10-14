"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# T O(n) S O(1)
def reverse_list1(head: Optional[ListNode]):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# T O(n) S O(n)
def reverse_list2(head: Optional[ListNode]):
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverse_list2(head.next)
        head.next.next = head
    head.next = None
    return new_head


def print_list(head: ListNode):
    itr = head
    out = ''
    while itr:
        out += str(itr.val) + "->"
        itr = itr.next

    print(out)


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

print_list(node1)
print_list(reverse_list2(node1))
