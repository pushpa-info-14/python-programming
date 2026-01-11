from collections import Counter
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = set()
        suffix = Counter(nums)
        initial = len(suffix)
        res = []
        for num in nums:
            prefix.add(num)
            suffix[num] -= 1
            if suffix[num] == 0:
                del suffix[num]
                initial -= 1
            res.append(len(prefix) - initial)
        return res


s = Solution()
print(s.distinctDifferenceArray(nums=[1, 2, 3, 4, 5]))
print(s.distinctDifferenceArray(nums=[3, 2, 3, 4, 2]))
