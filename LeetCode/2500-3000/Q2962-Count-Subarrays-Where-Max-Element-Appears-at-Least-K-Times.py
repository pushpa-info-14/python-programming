from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n, max_count = max(nums), 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_count += 1
            # while max_count > k or (l <= r and max_count == k and nums[l] != max_n):
            #     if nums[l] == max_n:
            #         max_count -= 1
            #     l += 1
            # if max_count == k:
            #     res += l + 1
            while max_count == k:
                if nums[l] == max_n:
                    max_count -= 1
                l += 1
            res += l
        return res


s = Solution()
print(s.countSubarrays([1, 3, 2, 3, 3], 2))
print(s.countSubarrays([1, 4, 2, 1], 3))
