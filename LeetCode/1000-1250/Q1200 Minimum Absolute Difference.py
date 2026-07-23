from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        min_diff = 10 ** 10
        res = []
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if min_diff > diff:
                min_diff = diff
                res = [[arr[i - 1], arr[i]]]
            elif min_diff == diff:
                res.append([arr[i - 1], arr[i]])
        return res


s = Solution()
print(s.minimumAbsDifference(arr=[4, 2, 1, 3]))
print(s.minimumAbsDifference(arr=[1, 3, 6, 10, 15]))
print(s.minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))
