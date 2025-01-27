from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        # 1. Find the longest cycle
        n = len(favorite)
        longest_cycle = 0
        visited = [False] * n
        length_2_cycles = []
        for i in range(n):
            if visited[i]:
                continue

            start, cur = i, i
            cur_set = set()
            while not visited[cur]:
                visited[cur] = True
                cur_set.add(cur)
                cur = favorite[cur]

            if cur in cur_set:
                length = len(cur_set)
                while start != cur:
                    length -= 1
                    start = favorite[start]
                longest_cycle = max(longest_cycle, length)
                if length == 2:
                    length_2_cycles.append([cur, favorite[cur]])

        # 2. Find sum of longest non-closed circles
        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src, parent):
            q = deque([(src, 0)])  # node, length
            max_length = 0

            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                max_length = max(max_length, length)
                for nei in inverted[node]:
                    q.append((nei, length + 1))
            return max_length

        chain_sum = 0
        for n1, n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2
        return max(chain_sum, longest_cycle)


s = Solution()
print(s.maximumInvitations([2, 2, 1, 2]))
print(s.maximumInvitations([1, 2, 0]))
print(s.maximumInvitations([3, 0, 1, 4, 1]))
