from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        nums = set(nums1 + nums2 + nums3)
        res = []
        for num in nums:
            if (num in set1 and num in set2) or (num in set2 and num in set3) or (num in set1 and num in set3):
                res.append(num)
        return res


s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
