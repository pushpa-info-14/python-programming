from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for digit in digits[::-1]:
            digit += carry
            res.append(digit % 10)
            carry = digit // 10
        if carry:
            res.append(1)
        return res[::-1]


s = Solution()
print(s.plusOne(digits=[1, 2, 3]))
print(s.plusOne(digits=[4, 3, 2, 1]))
print(s.plusOne(digits=[9]))
