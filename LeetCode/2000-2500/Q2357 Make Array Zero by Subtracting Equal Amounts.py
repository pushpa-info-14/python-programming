from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        cur = 0
        for num in nums:
            if num == 0:
                continue
            if num - cur == 0:
                continue
            cur = num
            res += 1
        return res


s = Solution()
print(s.minimumOperations(nums=[1, 5, 0, 3, 5]))
print(s.minimumOperations(nums=[0]))
