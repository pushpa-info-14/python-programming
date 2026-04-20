class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = -1
        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            mini = nums[i]
            for j in range(i + 1, n):
                mini = min(mini, nums[j])
            if (maxi - mini) <= k:
                res = i
                break
        return res


s = Solution()
print(s.firstStableIndex(nums=[5, 0, 1, 4], k=3))
print(s.firstStableIndex(nums=[3, 2, 1], k=1))
print(s.firstStableIndex(nums=[0], k=0))
