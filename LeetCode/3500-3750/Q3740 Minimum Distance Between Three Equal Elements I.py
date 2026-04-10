from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        inf = 10 ** 10
        res = inf
        mp = defaultdict(list)
        for idx, num in enumerate(nums):
            mp[num].append(idx)
            if len(mp[num]) > 2:
                i, j, k = mp[num][-3:]
                res = min(res, abs(i - j) + abs(j - k) + abs(k - i))
        return res if res != inf else -1


s = Solution()
print(s.minimumDistance(nums=[1, 2, 1, 1, 3]))
print(s.minimumDistance(nums=[1, 1, 2, 3, 2, 1, 2]))
print(s.minimumDistance(nums=[1]))
