from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        cur = head
        tail = head
        while cur:
            n += 1
            tail = cur
            cur = cur.next
        k %= n
        target = n - k
        count = 0
        cur = head
        while cur:
            count += 1
            if count == target:
                break
            cur = cur.next
        if cur.next:
            tail.next = head
            head = cur.next
            cur.next = None
        return head


s = Solution()
s.rotateRight(ListNode.create([1, 2, 3, 4, 5]), 2).print()
