from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid

        return l + k


s = Solution()
print(s.findKthPositive([2, 3, 4, 7, 11], 5))
print(s.findKthPositive([1, 2, 3, 4], 2))
print(s.findKthPositive([32, 59, 77], 1))
