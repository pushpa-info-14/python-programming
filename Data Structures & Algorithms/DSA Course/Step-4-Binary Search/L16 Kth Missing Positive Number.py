from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

    def findKthPositive2(self, arr: List[int], k: int) -> int:
        n = len(arr)

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k


s = Solution()
print(s.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(s.findKthPositive(arr=[1, 2, 3, 4], k=2))
print(s.findKthPositive2(arr=[2, 3, 4, 7, 11], k=5))
print(s.findKthPositive2(arr=[1, 2, 3, 4], k=2))
