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

    def maximumInvitations2(self, favorite: List[int]) -> int:
        n, longest_cycle, two_cycle_invitations = len(favorite), 0, 0
        in_degree = [0 for _ in range(n)]
        depth = [1 for _ in range(n)]

        for person in range(n):
            in_degree[favorite[person]] += 1

        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)

        while q:
            curr = q.popleft()
            next = favorite[curr]
            depth[next] = max(depth[next], depth[curr] + 1)
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)

        # only have cycles
        for person in range(n):
            if in_degree[person] == 0: continue
            cycle_length = 0
            curr = person
            while in_degree[curr] != 0:
                in_degree[curr] = 0
                cycle_length += 1
                curr = favorite[curr]
            if cycle_length == 2:
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)

s = Solution()
print(s.maximumInvitations([2, 2, 1, 2]))
print(s.maximumInvitations([1, 2, 0]))
print(s.maximumInvitations([3, 0, 1, 4, 1]))
print(s.maximumInvitations2([2, 2, 1, 2]))
print(s.maximumInvitations2([1, 2, 0]))
print(s.maximumInvitations2([3, 0, 1, 4, 1]))
