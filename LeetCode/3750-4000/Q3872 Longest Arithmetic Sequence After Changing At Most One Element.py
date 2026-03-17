from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        l = [2] * n
        r = [2] * n
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                l[i] = l[i - 1] + 1
        for i in range(n - 3, -1, -1):
            if nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]:
                r[i] = r[i + 1] + 1
        res = 2
        for i in range(n):
            if i > 0:
                res = max(res, l[i - 1] + 1)
            if i < n - 1:
                res = max(res, r[i + 1] + 1)
            if 0 < i < n - 1:
                if (nums[i + 1] - nums[i - 1]) % 2 == 0:
                    d = (nums[i + 1] - nums[i - 1]) // 2
                    l_len = 1
                    r_len = 1
                    if i >= 2 and nums[i - 1] - nums[i - 2] == d:
                        l_len = l[i - 1]
                    if i <= n - 3 and nums[i + 2] - nums[i + 1] == d:
                        r_len = r[i + 1]
                    res = max(res, l_len + r_len + 1)
        return res


s = Solution()
print(s.longestArithmetic(nums=[9, 7, 5, 10, 1]))
print(s.longestArithmetic(nums=[1, 2, 6, 7]))
