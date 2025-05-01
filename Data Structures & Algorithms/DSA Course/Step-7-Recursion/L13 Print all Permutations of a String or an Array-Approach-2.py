from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i):
            if i == n:
                res.append(nums.copy())
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return res


s = Solution()
print(s.permute([1, 2, 3]))
