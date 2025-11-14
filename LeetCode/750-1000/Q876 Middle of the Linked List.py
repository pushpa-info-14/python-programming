from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


s = Solution()
l = ListNode.create([1, 2, 3, 4, 5])
s.middleNode(l).print()
l = ListNode.create([1, 2, 3, 4, 5, 6])
s.middleNode(l).print()
