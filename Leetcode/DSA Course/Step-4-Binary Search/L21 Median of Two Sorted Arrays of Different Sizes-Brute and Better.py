from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        nums = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < n1:
            nums.append(nums1[i])
            i += 1
        while j < n2:
            nums.append(nums2[j])
            j += 1

        mid = n // 2
        if n % 2:
            return nums[mid]
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        index1 = n // 2 - 1
        index2 = n // 2
        element1 = -1
        element2 = -1
        counter = 0
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if index1 == counter: element1 = nums1[i]
                if index2 == counter: element2 = nums1[i]
                counter += 1
                i += 1
            else:
                if index1 == counter: element1 = nums2[j]
                if index2 == counter: element2 = nums2[j]
                counter += 1
                j += 1
        while i < n1:
            if index1 == counter: element1 = nums1[i]
            if index2 == counter: element2 = nums1[i]
            counter += 1
            i += 1
        while j < len(nums2):
            if index1 == counter: element1 = nums2[j]
            if index2 == counter: element2 = nums2[j]
            counter += 1
            j += 1

        if n % 2:
            return element2
        else:
            return (element1 + element2) / 2.0


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3, 4, 7, 10, 12], nums2=[2, 3, 6, 15]))
print(s.findMedianSortedArrays(nums1=[2, 3, 4], nums2=[1, 3]))
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))

print(s.findMedianSortedArrays2(nums1=[1, 3, 4, 7, 10, 12], nums2=[2, 3, 6, 15]))
print(s.findMedianSortedArrays2(nums1=[2, 3, 4], nums2=[1, 3]))
print(s.findMedianSortedArrays2(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays2(nums1=[1, 2], nums2=[3, 4]))
