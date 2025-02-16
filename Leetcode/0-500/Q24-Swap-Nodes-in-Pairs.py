from typing import Optional

from Leetcode.Common.ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev2 = None
        prev1 = dummy
        cur = head
        length = 1
        while cur:
            if length % 2 == 0:
                prev2.next = cur
                prev1.next = cur.next
                cur.next = prev1
                cur = prev1
            prev2 = prev1
            prev1 = cur
            cur = cur.next
            length += 1

        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

s = Solution()
print(s.swapPairs(head).print())
