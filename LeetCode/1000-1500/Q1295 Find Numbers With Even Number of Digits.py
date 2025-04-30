from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            count = 0
            while num:
                count += 1
                num //= 10
            if count % 2 == 0:
                res += 1
        return res


s = Solution()
print(s.findNumbers(nums=[12, 345, 2, 6, 7896]))
print(s.findNumbers(nums=[555, 901, 482, 1771]))
