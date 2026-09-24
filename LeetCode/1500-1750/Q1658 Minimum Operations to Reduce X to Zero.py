class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        res = -1
        l = 0
        cur = 0
        for r in range(n):
            cur += nums[r]
            while cur > target and l <= r:
                cur -= nums[l]
                l += 1
            if cur == target:
                res = max(res, r - l + 1)
        return res if res == -1 else n - res


s = Solution()
print(s.minOperations(nums=[1, 1, 4, 2, 3], x=5))
print(s.minOperations(nums=[5, 6, 7, 8, 9], x=4))
print(s.minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
