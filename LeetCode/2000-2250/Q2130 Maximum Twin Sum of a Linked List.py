from typing import Optional

from Common.ListNode import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p1 = head
        p2 = self.reverse(slow.next)
        res = 0
        while p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return res

    @staticmethod
    def reverse(head: ListNode) -> ListNode:
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


s = Solution()
ll = ListNode.create([5, 4, 2, 1])
print(s.pairSum(ll))
ll = ListNode.create([4, 2, 2, 3])
print(s.pairSum(ll))
ll = ListNode.create([1, 100000])
print(s.pairSum(ll))
