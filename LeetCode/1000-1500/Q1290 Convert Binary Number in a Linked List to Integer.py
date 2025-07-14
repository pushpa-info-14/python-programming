from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        digits = []
        cur = head
        while cur:
            digits.append(cur.val)
            cur = cur.next
        n = len(digits)
        res = 0
        power = 1
        for i in range(n):
            res += digits[n - i - 1] * power
            power <<= 1
        return res


s = Solution()
ls = ListNode(1, ListNode(0, ListNode(1)))
print(s.getDecimalValue(ls))
