from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def num_of_sub_arrays(k: int):
            if k < 0: return 0
            n = len(nums)
            l, r = 0, 0
            count = 0
            cur_sum = 0
            while r < n:
                cur_sum += nums[r] % 2

                while cur_sum > k:
                    cur_sum -= nums[l] % 2
                    l += 1
                count = count + r - l + 1
                r += 1
            return count

        return num_of_sub_arrays(k) - num_of_sub_arrays(k - 1)


s = Solution()
print(s.numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(s.numberOfSubarrays([2, 4, 6], 1))
print(s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
