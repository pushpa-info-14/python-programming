from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            pairs = 0
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    pairs += 1
            res += pairs
        return res

    def countPairs2(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        l, r = 0, n - 1
        while l < r:
            if nums[l] + nums[r] >= target:
                r -= 1
            else:
                res += r - l
                l += 1
        return res


s = Solution()
print(s.countPairs(nums=[-1, 1, 2, 3, 1], target=2))
print(s.countPairs2(nums=[-1, 1, 2, 3, 1], target=2))
print(s.countPairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2))
print(s.countPairs2(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2))
print(s.countPairs(nums=[9, -5, -5, 5, -5, -4, -6, 6, -6], target=3))
print(s.countPairs2(nums=[9, -5, -5, 5, -5, -4, -6, 6, -6], target=3))
