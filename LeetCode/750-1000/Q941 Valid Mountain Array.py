from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[0] >= arr[1]:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        if i != n - 1:
            return False
        return True


s = Solution()
print(s.validMountainArray(arr=[2, 1]))
print(s.validMountainArray(arr=[3, 5, 5]))
print(s.validMountainArray(arr=[0, 3, 2, 1]))
