from collections import defaultdict
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        delta = []
        for num in nums:
            delta.append((num ^ k) - num)

        delta.sort(reverse=True)

        result = sum(nums)
        for i in range(0, n, 2):
            if i + 1 >= n:
                continue
            pair_sum = delta[i] + delta[i + 1]
            if pair_sum > 0:
                result += pair_sum
        return result


s = Solution()
print(s.maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))
print(s.maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]]))
print(s.maximumValueSum(nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
print(s.maximumValueSum(nums=[24, 78, 1, 97, 44], k=6, edges=[[0, 2], [1, 2], [4, 2], [3, 4]]))  # 260
