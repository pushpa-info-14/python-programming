from typing import Optional, List

from Common.ListNode import ListNode


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        cur = head.next
        critical_points = []
        min_distance = 10 ** 10
        i = 0
        while cur.next:
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                critical_points.append(i)
                if len(critical_points) > 1:
                    min_distance = min(min_distance, critical_points[-1] - critical_points[-2])
            i += 1
            prev = cur
            cur = cur.next

        if len(critical_points) < 2:
            return [-1, -1]
        return [min_distance, critical_points[-1] - critical_points[0]]


s = Solution()
print(s.nodesBetweenCriticalPoints(ListNode.create([3, 1])))
print(s.nodesBetweenCriticalPoints(ListNode.create([5, 3, 1, 2, 5, 1, 2])))
print(s.nodesBetweenCriticalPoints(ListNode.create([1, 3, 2, 2, 3, 2, 2, 2, 7])))
