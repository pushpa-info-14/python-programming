import heapq
from typing import List

from Leetcode.Common.ListNode import ListNode


def merge(head1: ListNode, head2: ListNode):
    dummy = ListNode(-1)
    temp = dummy
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp.next = temp1
            temp1 = temp1.next
        else:
            temp.next = temp2
            temp2 = temp2.next
        temp = temp.next
    if temp1:
        temp.next = temp1
    if temp2:
        temp.next = temp2
    return dummy.next


def merge_lists(heads: List[ListNode]):
    if len(heads) == 1: return heads[0]

    temp = heads[0]
    for i in range(1, len(heads)):
        temp = merge(temp, heads[i])
    return temp


def merge_lists2(heads: List[ListNode]):
    n = len(heads)
    min_heap = []
    for i in range(n):
        heapq.heappush(min_heap, (heads[i].val, i))

    dummy = ListNode(-1)
    temp = dummy
    while min_heap:
        val, index = heapq.heappop(min_heap)
        temp.next = heads[index]
        heads[index] = heads[index].next
        if heads[index]:
            heapq.heappush(min_heap, (heads[index].val, index))
        temp = temp.next

    return dummy.next


l1 = ListNode.create([3])
l2 = ListNode.create([2, 10])
l3 = ListNode.create([1, 7, 11, 12])
l4 = ListNode.create([4, 9])
l5 = ListNode.create([5, 6, 8])

l = merge_lists([l1, l2, l3, l4, l5])
l.print()

l1 = ListNode.create([3])
l2 = ListNode.create([2, 10])
l3 = ListNode.create([1, 7, 11, 12])
l4 = ListNode.create([4, 9])
l5 = ListNode.create([5, 6, 8])

l = merge_lists2([l1, l2, l3, l4, l5])
l.print()
