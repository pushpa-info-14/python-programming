from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = counter[1]
        if res % 2 == 0:
            res -= 1
        del counter[1]
        for x in counter:
            cur = 0
            while counter[x] > 1:
                x = x * x
                cur += 2
            cur += 1 if counter[x] else -1
            res = max(res, cur)
        return res


s = Solution()
print(s.maximumLength(nums=[5, 4, 1, 2, 2]))
print(s.maximumLength(nums=[1, 3, 2, 4]))
print(s.maximumLength(nums=[1, 1]))
print(s.maximumLength(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]))
