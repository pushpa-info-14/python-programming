from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = 0
        zeros2 = 0
        sum1 = 0
        sum2 = 0
        for num in nums1:
            sum1 += num
            if num == 0:
                zeros1 += 1
        for num in nums2:
            sum2 += num
            if num == 0:
                zeros2 += 1

        sum1 += zeros1
        sum2 += zeros2

        if sum1 > sum2 and zeros2 == 0: return -1
        if sum1 < sum2 and zeros1 == 0: return -1

        return max(sum1, sum2)


s = Solution()
print(s.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0])) # 12
print(s.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4])) # -1
print(s.minSum(nums1=[0, 17, 20, 17, 5, 0, 14, 19, 7, 8, 16, 18, 6],
               nums2=[21, 1, 27, 19, 2, 2, 24, 21, 16, 1, 13, 27, 8, 5, 3, 11, 13, 7, 29, 7])) # 257
