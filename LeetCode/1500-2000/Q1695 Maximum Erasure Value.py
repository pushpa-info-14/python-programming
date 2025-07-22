from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur = 0
        seen = {}
        l = 0
        for i in range(n):
            num = nums[i]
            if num not in seen:
                seen[num] = i
                cur += num
            else:
                last = seen[num] + 1
                res = max(res, cur)
                for j in range(l, last):
                    cur -= nums[j]
                    del seen[nums[j]]
                seen[num] = i
                cur += num
                l = last
        res = max(res, cur)

        return res


s = Solution()
print(s.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(s.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
print(s.maximumUniqueSubarray(nums=
                              [187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266,
                               987, 965, 429, 166, 809, 340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189,
                               169, 743, 78, 810, 70, 382, 367, 490, 787, 670, 476, 278, 775, 673, 299, 19, 893, 817,
                               971, 458, 409, 886, 434]))
