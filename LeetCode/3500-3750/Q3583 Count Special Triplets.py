import bisect
from collections import defaultdict, Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)
        res = 0
        for i in range(n):
            num = nums[i]
            target = num * 2
            if target in mp:
                idx1 = bisect.bisect_left(mp[target], i)
                idx2 = bisect.bisect_right(mp[target], i)
                res += idx1 * (len(mp[target]) - idx2)
                res %= mod
        return res % mod

    def specialTriplets2(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        left = Counter()
        right = Counter(nums)
        res = 0
        for i in range(n):
            num = nums[i]
            target = num * 2
            right[num] -= 1
            res += left[target] * right[target]
            res %= mod
            left[num] += 1
        return res % mod


s = Solution()
print(s.specialTriplets(nums=[6, 3, 6]))
print(s.specialTriplets(nums=[0, 1, 0, 0]))
print(s.specialTriplets(nums=[8, 4, 2, 8, 4]))
print(s.specialTriplets2(nums=[6, 3, 6]))
print(s.specialTriplets2(nums=[0, 1, 0, 0]))
print(s.specialTriplets2(nums=[8, 4, 2, 8, 4]))
