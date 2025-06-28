from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        num_to_index = [(num, i) for i, num in enumerate(nums)]
        num_to_index.sort(reverse=True)

        index_to_num = [(i, num) for num, i in num_to_index[:k]]
        index_to_num.sort()

        return [num for _, num in index_to_num]


s = Solution()
print(s.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(s.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
print(s.maxSubsequence(nums=[3, 4, 3, 3], k=2))
