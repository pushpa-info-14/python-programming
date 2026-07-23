from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_nums = set(arr)
        nums = sorted(unique_nums)
        rank = {}
        for i in range(len(nums)):
            rank[nums[i]] = i + 1
        res = []
        for x in arr:
            res.append(rank[x])
        return res


s = Solution()
print(s.arrayRankTransform(arr=[40, 10, 20, 30]))
print(s.arrayRankTransform(arr=[100, 100, 100]))
print(s.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
