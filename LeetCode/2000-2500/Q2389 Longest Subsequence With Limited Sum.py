import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for query in queries:
            cur = 0
            cur_size = 0
            for num in nums:
                cur += num
                if cur <= query:
                    cur_size += 1
                if cur > query:
                    break
            res.append(cur_size)
        return res

    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        res = []
        for query in queries:
            index = bisect.bisect_right(pre_sum, query)
            res.append(index - 1)
        return res


s = Solution()
print(s.answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
print(s.answerQueries(nums=[2, 3, 4, 5], queries=[1]))
print("------------------")
print(s.answerQueries2(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
print(s.answerQueries2(nums=[2, 3, 4, 5], queries=[1]))
