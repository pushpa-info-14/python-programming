import math
from collections import defaultdict
from typing import List


def reverse(x):
    num = 0
    while x:
        num *= 10
        num += x % 10
        x //= 10
    return num


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        res = math.inf
        for i in range(n):
            num = nums[i]
            if num in mp:
                j = mp[num]
                res = min(res, abs(i - j))
            x = reverse(num)
            mp[x] = i
        return res if res != math.inf else -1


s = Solution()
print(s.minMirrorPairDistance(nums=[12, 21, 45, 33, 54]))
print(s.minMirrorPairDistance(nums=[120, 21]))
print(s.minMirrorPairDistance(nums=[21, 120]))
