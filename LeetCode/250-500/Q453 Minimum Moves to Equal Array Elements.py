class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        res = 0
        for num in nums:
            res += num - mn
        return res


s = Solution()
print(s.minMoves(nums=[1, 2, 3]))
print(s.minMoves(nums=[1, 1, 1]))
