from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur.val == 0 and cur.next:
                temp = cur.next
                total = 0
                while temp and temp.val != 0:
                    total += temp.val
                    temp = temp.next
                cur.val = total
                if not temp.next: # avoid last 0
                    cur.next = None
                else:
                    cur.next = temp
                cur = temp
            else:
                return head
        return head


s = Solution()
head = ListNode.create([0, 3, 1, 0, 4, 5, 2, 0])
s.mergeNodes(head).print()
