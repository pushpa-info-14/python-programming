from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        inf = 10 ** 10
        n = len(edges)

        def traverse(node):
            distance = [inf] * n
            cur = node
            count = 0
            while cur != -1:
                distance[cur] = count
                count += 1
                cur = edges[cur]
                if distance[cur] != inf:
                    break
            return distance

        d1 = traverse(node1)
        d2 = traverse(node2)

        best = inf
        best_index = 0
        for index, (a, b) in enumerate(zip(d1, d2)):
            if max(a, b) < best:
                best = max(a, b)
                best_index = index

        if best == inf:
            return -1
        return best_index


s = Solution()
print(s.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))  # 2
print(s.closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2))  # 2
print(s.closestMeetingNode(edges=[4, 4, 4, 5, 1, 2, 2], node1=1, node2=1))
print(s.closestMeetingNode(edges=[4, 4, 8, -1, 9, 8, 4, 4, 1, 1], node1=5, node2=6))
