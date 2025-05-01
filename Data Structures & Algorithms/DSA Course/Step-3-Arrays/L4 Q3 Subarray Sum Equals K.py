from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = {}
        res = 0
        cur_sum = 0

        for i in range(n):
            cur_sum += nums[i]

            if cur_sum == k:
                res += 1
            rem = cur_sum - k
            if rem in pre_sum:
                res += pre_sum[rem]
            if cur_sum not in pre_sum:
                pre_sum[cur_sum] = 0
            pre_sum[cur_sum] += 1

        return res


s = Solution()
print(s.subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))  # 55
