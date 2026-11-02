class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        target = nums[n // 2]
        res = 0
        for num in nums:
            res += abs(target - num)
        return res


s = Solution()
print(s.minMoves2(nums=[1, 2, 3]))  # 2
print(s.minMoves2(nums=[1, 10, 2, 9]))  # 16
print(s.minMoves2(nums=[1, 2, 3, 28]))  # 28
print(s.minMoves2(nums=[10, 10, 1, 10, 5]))  # 14
