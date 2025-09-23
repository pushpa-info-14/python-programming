from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            val = -1
            found = False
            for j in nums2:
                if i == j:
                    found = True
                if found and i < j:
                    val = j
                    break
            res.append(val)

        return res

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums2):
            mapping[num] = i
        res = []
        for num1 in nums1:
            val = -1
            match = mapping[num1]
            for j in range(match, len(nums2)):
                if num1 < nums2[j]:
                    val = nums2[j]
                    break
            res.append(val)

        return res

    def nextGreaterElement3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index = {}
        for i, num in enumerate(nums1):
            nums1_index[num] = i
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = nums1_index[val]
                res[index] = cur
            if cur in nums1_index:
                stack.append(cur)
        return res


s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(s.nextGreaterElement2([4, 1, 2], [1, 3, 4, 2]))
print(s.nextGreaterElement3([4, 1, 2], [1, 3, 4, 2]))
