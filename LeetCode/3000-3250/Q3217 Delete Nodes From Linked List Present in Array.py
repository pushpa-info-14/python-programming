from typing import List, Optional

from Common.ListNode import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


s = Solution()
head = ListNode.create([1, 2, 3, 4, 5])
s.modifiedList([1, 2, 3], head).print()
