# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        target = length - n

        cur = dummy
        while target > 0:
            cur = cur.next
            target -= 1

        cur.next = cur.next.next

        return dummy.next


def print_list(head: ListNode):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
print_list(s.removeNthFromEnd(head, 2))
