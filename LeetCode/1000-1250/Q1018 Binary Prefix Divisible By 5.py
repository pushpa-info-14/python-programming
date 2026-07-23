from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for bit in nums:
            x = (2 * x + bit) % 5
            if x == 0:
                res.append(True)
            else:
                res.append(False)
        return res


s = Solution()
print(s.prefixesDivBy5(nums=[0, 1, 1]))
print(s.prefixesDivBy5(nums=[1, 1, 1]))
