class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        res = n
        l, r = -1, -1
        for i in range(n):
            if nums[i] == 1:
                l = i
            elif nums[i] == 2:
                r = i
            if l != -1 and r != -1:
                res = min(res, abs(r - l))
        return res if res != n else -1


s = Solution()
print(s.minAbsoluteDifference(nums=[1, 0, 0, 2, 0, 1]))
print(s.minAbsoluteDifference(nums=[1, 0, 1, 0]))
