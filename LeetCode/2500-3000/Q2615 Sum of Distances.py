from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)
        for num in set(nums):
            size = len(mp[num])
            cur = mp[num]
            pfx_sum = [0] * size
            sfx_sum = [0] * size
            for i in range(size):
                pfx_sum[i] = cur[i] + (pfx_sum[i - 1] if i > 0 else 0)
            for i in range(size - 1, -1, -1):
                sfx_sum[i] = cur[i] + (sfx_sum[i + 1] if i < size - 1 else 0)
            for i in range(size):
                nums[cur[i]] = i * cur[i] - pfx_sum[i] + sfx_sum[i] - (size - i - 1) * cur[i]
        return nums


s = Solution()
print(s.distance(nums=[1, 3, 1, 1, 2]))
print(s.distance(nums=[0, 5, 3]))
