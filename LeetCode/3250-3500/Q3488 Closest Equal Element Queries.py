import bisect
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        inf = 10 ** 10
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)
        res = []
        for i in queries:
            num = nums[i]
            cur = inf
            size = len(mp[num])
            if size > 1:
                idx = bisect.bisect_left(mp[num], i)
                d = abs(i - mp[num][idx - 1])
                cur = min(cur, d, n - d)
                d = abs(mp[num][(idx + 1) % size] - i)
                cur = min(cur, d, n - d)
            res.append(cur if cur != inf else -1)
        return res

    def solveQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        inf = 10 ** 10
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)
        res = []
        for i in queries:
            num = nums[i]
            cur = inf
            size = len(mp[num])
            if size > 1:
                idx = bisect.bisect_left(mp[num], i)
                if idx == 0:
                    l, r = mp[num][-1] - n, mp[num][idx + 1]
                elif idx == size - 1:
                    l, r = mp[num][idx - 1], mp[num][0] + n
                else:
                    l, r = mp[num][idx - 1], mp[num][idx + 1]
                cur = min(cur, i - l, r - i)
            res.append(cur if cur != inf else -1)
        return res


s = Solution()
print(s.solveQueries(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5]))
print(s.solveQueries(nums=[1, 2, 3, 4], queries=[0, 1, 2, 3]))
print(s.solveQueries(nums=[14, 14, 4, 2, 19, 19, 14, 19, 14], queries=[2, 4, 8, 6, 3]))
print("------------")
print(s.solveQueries2(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5]))
print(s.solveQueries2(nums=[1, 2, 3, 4], queries=[0, 1, 2, 3]))
print(s.solveQueries2(nums=[14, 14, 4, 2, 19, 19, 14, 19, 14], queries=[2, 4, 8, 6, 3]))
