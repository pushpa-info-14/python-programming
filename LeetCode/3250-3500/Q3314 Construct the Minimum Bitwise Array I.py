from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            cur = - 1
            for candidate in range(num):
                if candidate | (candidate + 1) == num:
                    cur = candidate
                    break
            res.append(cur)
        return res


s = Solution()
print(s.minBitwiseArray(nums=[2, 3, 5, 7]))
print(s.minBitwiseArray(nums=[11, 13, 31]))
