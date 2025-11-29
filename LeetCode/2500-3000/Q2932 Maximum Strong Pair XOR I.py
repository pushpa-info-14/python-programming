from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                x, y = nums[i], nums[j]
                if y > 2 * x:
                    break
                res = max(res, x ^ y)
        return res


s = Solution()
print(s.maximumStrongPairXor(nums=[1, 2, 3, 4, 5]))
print(s.maximumStrongPairXor(nums=[10, 100]))
print(s.maximumStrongPairXor(nums=[5, 6, 25, 30]))
