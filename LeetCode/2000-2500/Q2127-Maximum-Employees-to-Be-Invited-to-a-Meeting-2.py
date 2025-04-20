from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
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
