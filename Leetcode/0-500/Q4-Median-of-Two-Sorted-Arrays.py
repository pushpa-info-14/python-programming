from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2  # nums1
            j = half - i - 2  # nums2

            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float("infinity")
            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float("infinity")

            # partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # odd
                if total % 2:
                    return min(nums1_right, nums2_right)
                # even
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1


# log(min(m,n))
s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3,4]))
print(s.findMedianSortedArrays([], [1]))
