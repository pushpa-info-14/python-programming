# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        q = []
        for i in range(n):
            if lists[i] is not None:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next

        dummy = ListNode(0)
        cur = dummy
        while q:
            val, index = heapq.heappop(q)
            cur.next = ListNode(val)
            if lists[index]:
                heapq.heappush(q, (lists[index].val, index))
                lists[index] = lists[index].next
            cur = cur.next
        return dummy.next


def print_list(head: ListNode):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


head1 = ListNode(1, ListNode(4, ListNode(5)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
head3 = ListNode(2, ListNode(6))

s = Solution()
print_list(s.mergeKLists([head1, head2, head3]))
