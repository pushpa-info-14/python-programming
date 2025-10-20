from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            odd = set()
            even = set()
            for j in range(i, n):
                if nums[j] & 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(odd) == len(even):
                    res = max(res, j - i + 1)
        return res


s = Solution()
print(s.longestBalanced(nums=[2, 5, 4, 3]))
print(s.longestBalanced(nums=[3, 2, 2, 5, 4]))
print(s.longestBalanced(nums=[1, 2, 3, 2]))
