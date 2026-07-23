from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (limit * 2 + 2)
        for i in range(len(nums) // 2):
            a, b = sorted((nums[i], nums[n - 1 - i]))
            diff[2] += 2
            diff[1 + a] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[limit + b + 1] += 1

        res = n
        moves = 0
        for target in range(2, limit * 2 + 1):
            moves += diff[target]
            res = min(res, moves)
        return res


s = Solution()
print(s.minMoves(nums=[1, 2, 4, 3], limit=4)) # 1
print(s.minMoves(nums=[1, 2, 2, 1], limit=2)) # 2
print(s.minMoves(nums=[1, 2, 1, 2], limit=2)) # 0
