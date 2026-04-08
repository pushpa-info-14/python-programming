from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % mod
                idx += k
        res = 0
        for num in nums:
            res ^= num
        return res


s = Solution()
print(s.xorAfterQueries(nums=[1, 1, 1], queries=[[0, 2, 1, 4]]))
print(s.xorAfterQueries(nums=[2, 3, 1, 5, 4], queries=[[1, 4, 2, 3], [0, 2, 1, 2]]))
