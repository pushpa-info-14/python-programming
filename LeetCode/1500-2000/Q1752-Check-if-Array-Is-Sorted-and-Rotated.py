from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        count = 1
        for i in range(1, 2 * n):
            if nums[(i - 1) % n] <= nums[i % n]:
                count += 1
            else:
                count = 1
            if count == n:
                return True
        return False


s = Solution()
print(s.check([3, 4, 5, 1, 2]))
print(s.check([2, 1, 3, 4]))
print(s.check([1, 2, 3]))
