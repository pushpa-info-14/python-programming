from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        m = len(conflictingPairs)
        # Ensure each pair is ordered (start <= end)
        for p in conflictingPairs:
            if p[0] > p[1]:
                p[0], p[1] = p[1], p[0]
        # Sort by end-point
        conflictingPairs.sort(key=lambda x: x[1])

        blocked = 0
        profit = 0
        max_profit = 0
        max1 = 0
        max2 = 0

        for i, (start, end) in enumerate(conflictingPairs):
            bottom = conflictingPairs[i + 1][1] if i < m - 1 else n + 1
            gap = bottom - end

            if start > max1:
                max2 = max1
                max1 = start
                profit = 0
            elif start > max2:
                max2 = start

            profit += (max1 - max2) * gap
            if profit > max_profit:
                max_profit = profit

            blocked += max1 * gap

        total_sub_arrays = n * (n + 1) // 2
        return total_sub_arrays - blocked + max_profit


s = Solution()
print(s.maxSubarrays(n=4, conflictingPairs=[[2, 3], [1, 4]]))
print(s.maxSubarrays(n=5, conflictingPairs=[[1, 2], [2, 5], [3, 5]]))
