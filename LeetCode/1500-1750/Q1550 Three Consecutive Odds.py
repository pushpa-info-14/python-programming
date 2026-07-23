from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        l = 0
        for r in range(n):
            if arr[r] % 2 == 0:
                l = r + 1
            if r - l + 1 == 3:
                return True
        return False


s = Solution()
print(s.threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(s.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))
