from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            max_digit = max(digits)
            encrypted = max_digit
            for i in range(len(digits) - 1):
                encrypted *= 10
                encrypted += max_digit
            res += encrypted
        return res


s = Solution()
print(s.sumOfEncryptedInt(nums=[1, 2, 3]))
print(s.sumOfEncryptedInt(nums=[10, 21, 31]))
