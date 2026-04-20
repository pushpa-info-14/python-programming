class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prev_greater = [-1] * n
        next_smaller = [-1] * n
        cur = nums[0]
        for i in range(n):
            cur = max(cur, nums[i])
            prev_greater[i] = cur
        cur = nums[-1]
        for i in range(n - 1, -1, -1):
            cur = min(cur, nums[i])
            next_smaller[i] = cur

        res = -1
        for i in range(n):
            maxi = max(nums[i], prev_greater[i])
            mini = min(nums[i], next_smaller[i])
            if (maxi - mini) <= k:
                res = i
                break
        return res


s = Solution()
print(s.firstStableIndex(nums=[5, 0, 1, 4], k=3))
print(s.firstStableIndex(nums=[3, 2, 1], k=1))
print(s.firstStableIndex(nums=[0], k=0))
