from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # number of sub-arrays less than or equal to goal
        def num_of_sub_arrays(target: int):
            if target < 0: return 0

            n = len(nums)
            l, r = 0, 0
            res = 0
            cur_sum = 0

            while r < n:
                cur_sum += nums[r]

                while cur_sum > target:
                    cur_sum -= nums[l]
                    l += 1
                res = res + r - l + 1

                r += 1
            return res

        return num_of_sub_arrays(goal) - num_of_sub_arrays(goal - 1)


s = Solution()
print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(s.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
