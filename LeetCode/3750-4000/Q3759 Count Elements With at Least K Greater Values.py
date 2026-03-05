from collections import Counter
from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        counter = Counter(nums)
        res = 0
        cur = n
        i = 0
        while i < n:
            num = nums[i]
            if (cur - counter[num]) >= k:
                res += counter[num]
            cur -= counter[num]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res


s = Solution()
print(s.countElements(nums=[3, 1, 2], k=1))
print(s.countElements(nums=[5, 5, 5], k=2))
