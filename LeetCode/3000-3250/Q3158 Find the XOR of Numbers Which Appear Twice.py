from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for num in nums:
            if num in seen:
                res ^= num
            else:
                seen.add(num)
        return res


s = Solution()
print(s.duplicateNumbersXOR(nums=[1, 2, 1, 3]))
print(s.duplicateNumbersXOR(nums=[1, 2, 3]))
print(s.duplicateNumbersXOR(nums=[1, 2, 2, 1]))
