from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        rem_to_idx = {0: -1}
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            prefix = (cur_sum - rem + p) % p
            if prefix in rem_to_idx:
                res = min(res, i - rem_to_idx[prefix])
            rem_to_idx[cur_sum] = i

        return -1 if res == len(nums) else res


s = Solution()
print(s.minSubarray(nums=[3, 1, 4, 2], p=6))
print(s.minSubarray(nums=[6, 3, 5, 2], p=9))
print(s.minSubarray(nums=[1, 2, 3], p=3))
