from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head


s = Solution()
ll = ListNode.create([1, 3, 4, 7, 1, 2, 6])
s.deleteMiddle(ll).print()
