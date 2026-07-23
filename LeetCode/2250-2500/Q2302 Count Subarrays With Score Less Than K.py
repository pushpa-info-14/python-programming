from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        range_sum = 0
        l = 0
        for r in range(n):
            range_sum += nums[r]
            while range_sum * (r - l + 1) >= k:
                range_sum -= nums[l]
                l += 1
            res += r - l + 1

        return res


s = Solution()
print(s.countSubarrays(nums=[2, 1, 4, 3, 5], k=10))
print(s.countSubarrays(nums=[1, 1, 1], k=5))
