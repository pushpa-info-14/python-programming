from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while True:
            idx = 0
            pair_sum = 10 ** 10
            is_non_decreasing = True
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    is_non_decreasing = False
                cur = nums[i - 1] + nums[i]
                if pair_sum > cur:
                    pair_sum = cur
                    idx = i
            if is_non_decreasing:
                break
            else:
                res += 1
                nums = nums[:idx - 1] + [pair_sum] + nums[idx + 1:]
        return res


s = Solution()
print(s.minimumPairRemoval(nums=[5, 2, 3, 1]))
print(s.minimumPairRemoval(nums=[1, 2, 2]))
