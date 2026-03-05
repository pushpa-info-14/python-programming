from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 10 ** 20
        l = 0
        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            res = min(res, n - (r - l + 1))
        return res


s = Solution()
print(s.minRemoval(nums=[2, 1, 5], k=2))
print(s.minRemoval(nums=[1, 6, 2, 9], k=3))
print(s.minRemoval(nums=[4, 6], k=2))
print(s.minRemoval(nums=[68, 54, 14, 59], k=4))
