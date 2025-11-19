from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            count = 0
            seen = set()
            for j in range(i, n):
                num = nums[j]
                if num not in seen:
                    seen.add(num)
                    count += 1
                res += count * count
        return res


s = Solution()
print(s.sumCounts(nums=[1, 2, 1]))
print(s.sumCounts(nums=[1, 1]))
