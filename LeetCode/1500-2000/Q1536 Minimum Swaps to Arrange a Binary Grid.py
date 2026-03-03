from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def left_most_zeros(nums):
            count = 0
            for i in reversed(range(len(nums))):
                if nums[i] != 0:
                    break
                count += 1
            return count

        res = 0
        rows = [left_most_zeros(row) for row in grid]
        for i in range(n):
            target = n - i - 1
            if rows[i] >= target:
                continue
            found = False
            for j in range(i + 1, n):
                if rows[j] >= target:
                    res += j - i
                    for k in range(j, i, -1):
                        rows[k] = rows[k - 1]
                    found = True
                    break
            if not found:
                return -1
        return res


s = Solution()
print(s.minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(s.minSwaps(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(s.minSwaps(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
