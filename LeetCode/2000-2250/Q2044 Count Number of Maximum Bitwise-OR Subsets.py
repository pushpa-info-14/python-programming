from collections import defaultdict
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)

        def dfs(index, current):
            if index == n:
                freq[current] += 1
                return
            # Ignore current element
            dfs(index + 1, current)

            # Consider current element
            dfs(index + 1, current | nums[index])

        dfs(0, 0)

        return freq[max(freq.keys())]


s = Solution()
print(s.countMaxOrSubsets(nums=[3, 1]))
print(s.countMaxOrSubsets(nums=[2, 2, 2]))
