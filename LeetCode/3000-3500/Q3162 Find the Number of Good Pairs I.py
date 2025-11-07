from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        res = 0
        for i in range(n):
            num = nums1[i]
            if num % k != 0:
                continue
            for j in range(m):
                if num % (nums2[j] * k) == 0:
                    res += 1
        return res


s = Solution()
print(s.numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
print(s.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
