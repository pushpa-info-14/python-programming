from typing import Optional

from Common.ListNode import ListNode


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            g = gcd(cur.val, cur.next.val)
            gcd_node = ListNode(g)
            temp = cur.next
            cur.next = gcd_node
            gcd_node.next = temp
            cur = temp
        return head


s = Solution()
head = ListNode.create([18, 6, 10, 3])
s.insertGreatestCommonDivisors(head).print()
