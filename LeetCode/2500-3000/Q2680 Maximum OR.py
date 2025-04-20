from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_or = [0] * n
        suffix_or = [0] * n
        cur_prefix = 0
        cur_suffix = 0
        for i in range(n):
            prefix_or[i] = cur_prefix
            suffix_or[n - i - 1] = cur_suffix
            cur_prefix |= nums[i]
            cur_suffix |= nums[n - i - 1]

        res = 0
        for i, num in enumerate(nums):
            num = num << k
            cur_or = prefix_or[i] | num | suffix_or[i]
            res = max(res, cur_or)
        return res


s = Solution()
print(s.maximumOr(nums=[12, 9], k=1))
print(s.maximumOr(nums=[8, 1, 2], k=2))
