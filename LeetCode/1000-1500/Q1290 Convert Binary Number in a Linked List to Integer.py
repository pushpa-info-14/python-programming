from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        cur = head
        while cur:
            res = (res << 1) + cur.val
            cur = cur.next
        return res


s = Solution()
ls = ListNode(1, ListNode(0, ListNode(1)))
print(s.getDecimalValue(ls))
