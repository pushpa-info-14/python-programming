from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(logs)
        logs.sort(key=lambda t: t[1])
        query_map = []
        for i in range(len(queries)):
            query_map.append([queries[i], i])
        query_map.sort()
        l, r = 0, 0
        mp = defaultdict(int)
        res = [0] * len(queries)
        for query, i in query_map:
            while r < m and logs[r][1] <= query:
                mp[logs[r][0]] = logs[r][1]
                r += 1
            while l < r and logs[l][1] < query - x:
                if mp[logs[l][0]] < query - x:
                    del mp[logs[l][0]]
                l += 1
            res[i] = n - len(mp.keys())
        return res


s = Solution()
print(s.countServers(n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11]))
print(s.countServers(n=3, logs=[[2, 4], [2, 1], [1, 2], [3, 1]], x=2, queries=[3, 4]))
print(s.countServers(n=6, logs=[[1, 21]], x=10, queries=[24, 35, 28, 26, 20, 25, 16, 31, 12]))
