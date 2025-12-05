from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        1011 - 11
        1001 - 9
        1010 - 10 9 | 10 = 11

        1101 - 13
        1100 - 12
        1101 - 13 12 | 13 = 13

        11111 - 31
         1111 - 15
        10000 - 16 15 | 16 = 31
        """
        res = []
        for num in nums:
            if num == 2:
                res.append(-1)
                continue

            b = bin(num).lstrip('0b')
            set_bits = b.count('1')
            if len(b) == set_bits:
                res.append(int('1' * (set_bits - 1), 2))
            else:
                idx = b.rfind('0')
                digits = list(b)
                digits[idx + 1] = '0'
                res.append(int(''.join(digits), 2))
        return res


s = Solution()
print(s.minBitwiseArray(nums=[2, 3, 5, 7]))
print(s.minBitwiseArray(nums=[11, 13, 31]))
