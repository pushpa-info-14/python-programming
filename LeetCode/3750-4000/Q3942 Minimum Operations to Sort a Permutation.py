from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        point = 0
        point_index = 0
        inc_count = 0
        dec_count = 0
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                inc_count += 1
            elif nums[i - 1] - 1 == nums[i]:
                dec_count += 1
            else:
                point += 1
                point_index = i
        if inc_count > 0 and dec_count > 0:
            return -1
        if point == 0:
            return 0 if nums[0] < nums[-1] else 1
        elif point == 1:
            p1 = nums[:point_index]
            p2 = nums[point_index:]
            res = n
            if p1[-1] > p2[0]:  # increasing and rotated
                res = min(res, len(p1), len(p2) + 2)
            else:  # decreasing and rotated
                res = min(res, len(p1) + 1, len(p2) + 1)
            return res
        else:
            return -1


s = Solution()
print(s.minOperations(nums=[0, 2, 1]))
print(s.minOperations(nums=[1, 0, 2]))
print(s.minOperations(nums=[2, 0, 1, 3]))
print(s.minOperations(nums=[1, 2, 0]))
print(s.minOperations(nums=[1, 2, 3, 0]))
print(s.minOperations(nums=[0, 1, 3, 2]))
print(s.minOperations(nums=[1, 2, 3, 4, 0]))
print(s.minOperations(nums=[1, 2]))
print(s.minOperations(nums=[2, 1]))
print(s.minOperations(nums=[1]))
