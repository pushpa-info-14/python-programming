from itertools import accumulate
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 10 ** 20
        res = -inf
        i = 0
        while i < n:
            # Shortest first segment
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue

            curr = nums[p] + nums[p - 1]

            # Full second segment
            while j < n and nums[j] < nums[j - 1]:
                curr += nums[j]
                j += 1
            q = j - 1

            if p == q or q == n - 1 or (q < n - 1 and nums[q] == nums[j]):
                i = q
                continue

            # Third segment with max sum
            curr += nums[j]
            j += 1

            acc = 0
            mx = 0
            while j < n and nums[j] > nums[j - 1]:
                acc += nums[j]
                mx = max(mx, acc)
                j += 1
            curr += mx

            # Maximize the sum of first segment
            acc = 0
            mx = 0
            jj = p - 2
            while jj >= 0 and nums[jj] < nums[jj + 1]:
                acc += nums[jj]
                mx = max(mx, acc)
                jj -= 1
            curr += mx

            res = max(res, curr)
            i = q  # Next possible trionic starts with the last segment
        return res

    def maxSumTrionic2(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 10 ** 20
        res = -inf
        l = p = q = r = 0
        while l < n:
            p = l
            while p + 1 < n and nums[p] < nums[p + 1]:
                p += 1
            if l == p:
                l += 1
                continue
            q = p
            while q + 1 < n and nums[q] > nums[q + 1]:
                q += 1
            if p == q:
                l = q + 1
                continue
            r = q
            while r + 1 < n and nums[r] < nums[r + 1]:
                r += 1
            if r == q:
                l = r + 1
                continue
            res = max(res,
                       max(accumulate(reversed(nums[l:p]))) + sum(nums[p:q + 1]) + max(accumulate(nums[q + 1:r + 1])))
            l = q
        return res


s = Solution()
print(s.maxSumTrionic(nums=[0, -2, -1, -3, 0, 2, -1]))  # -4
print(s.maxSumTrionic(nums=[1, 4, 2, 7]))  # 14
print(s.maxSumTrionic(nums=[1, 4, 2, 2, 3, 1, 2]))  # 8
print("---------")
print(s.maxSumTrionic2(nums=[0, -2, -1, -3, 0, 2, -1]))  # -4
print(s.maxSumTrionic2(nums=[1, 4, 2, 7]))  # 14
print(s.maxSumTrionic2(nums=[1, 4, 2, 2, 3, 1, 2]))  # 8
