from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return 0


s = Solution()
print(s.repeatedNTimes(nums=[1, 2, 3, 3]))
print(s.repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]))
print(s.repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]))
