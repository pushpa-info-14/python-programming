from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        cur = 0
        for r in range(n):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            res = max(res, r - l + 1)
            cur = cur | nums[r]
            # cur = cur ^ nums[r]

        return res

    def longestNiceSubarray2(self, nums: List[int]) -> int:
        res = 1
        prev = l = 0
        for r in range(len(nums)):
            while (prev & (prev + nums[r])) != prev:
                prev -= nums[l]
                l += 1
            prev += nums[r]
            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.longestNiceSubarray([1, 3, 8, 48, 10]))
print(s.longestNiceSubarray2([1, 3, 8, 48, 10]))
