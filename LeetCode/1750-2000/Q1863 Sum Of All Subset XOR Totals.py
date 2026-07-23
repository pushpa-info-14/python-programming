from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, xor):
            if i == n:
                return xor

            return dfs(i + 1, xor) + dfs(i + 1, xor ^ nums[i])

        return dfs(0, 0)

    def subsetXORSum2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in nums:
            res = res | num
        return res << (n - 1)


s = Solution()
print(s.subsetXORSum([1, 3]))
print(s.subsetXORSum([5, 1, 6]))
print(s.subsetXORSum([3, 4, 5, 6, 7, 8]))
print(s.subsetXORSum2([1, 3]))
print(s.subsetXORSum2([5, 1, 6]))
print(s.subsetXORSum2([3, 4, 5, 6, 7, 8]))
