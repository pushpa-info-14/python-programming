from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        diff = [0] * (n + 1)
        summation = 0
        pos = 0
        for i in range(n):
            while summation + diff[i] < nums[i]:
                if pos == q:  # All queries done
                    return -1

                start, end, val = queries[pos]
                pos += 1

                if end < i: continue  # Skip past update

                # Range update in O(1)
                diff[max(start, i)] += val
                diff[end + 1] -= val
            summation += diff[i]
        return pos


s = Solution()
print(s.minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(s.minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
