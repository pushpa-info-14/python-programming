from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        for num in arr1:
            while num and num not in prefix_set:
                prefix_set.add(num)
                num = num // 10

        res = 0
        for num in arr2:
            while num and num not in prefix_set:
                num = num // 10

            if num:
                res = max(res, len(str(num)))
        return res


s = Solution()
print(s.longestCommonPrefix([1, 10, 100], [1000]))
print(s.longestCommonPrefix([1, 2, 3], [4, 4, 4]))
