import bisect
from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        inf = 10 ** 10
        mp = [(v, i) for i, v in enumerate(nums)]
        mp.sort()
        ntoi = {}
        for i, (_, idx) in enumerate(mp):
            ntoi[idx] = i

        max_jumps = [0] * n
        for i, (v, idx) in enumerate(mp):
            nxt = bisect.bisect_left(mp, (v + maxDiff, inf)) - 1
            max_jumps[i] = nxt

        log = n.bit_length()
        up = [max_jumps]
        for _ in range(1, log):
            last = up[-1]
            up.append([last[last[i]] for i in range(n)])

        res = []
        for a, b in queries:
            a = ntoi[a]
            b = ntoi[b]
            if a == b:
                res.append(0)
                continue
            if a > b:
                a, b = b, a
            cur = a
            jumps = 0
            for k in range(log - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    jumps += 2 ** k
            if max_jumps[cur] >= b:
                res.append(jumps + 1)
            else:
                res.append(-1)
        return res


s = Solution()
print(s.pathExistenceQueries(n=5, nums=[1, 8, 3, 4, 2], maxDiff=3, queries=[[0, 3], [2, 4]]))
print(s.pathExistenceQueries(n=5, nums=[5, 3, 1, 9, 10], maxDiff=2, queries=[[0, 1], [0, 2], [2, 3], [4, 3]]))
print(s.pathExistenceQueries(n=3, nums=[3, 6, 1], maxDiff=1, queries=[[0, 0], [0, 1], [1, 2]]))
