from functools import cache


class Solution:
    @staticmethod
    def getSumWaviness(num: str) -> int:
        n = len(num)

        @cache
        def ddp(idx, tight, started, ld, sld):
            if idx == n:
                return 1, 0  # possible, wavySum

            possible = 0
            local_wavy_sum = 0
            limit = int(num[idx]) if tight else 9
            for d in range(limit + 1):
                next_tight = tight and d == limit
                next_start = started or d > 0
                is_wavy = 0
                if ld != -1 and sld != -1:
                    if (d > ld < sld) or (d < ld > sld):
                        is_wavy = 1

                poss, wavy = ddp(idx + 1, next_tight, next_start, d if next_start else -1, ld if next_start else -1)
                possible += poss
                local_wavy_sum += wavy + (poss * is_wavy)
            return possible, local_wavy_sum

        return ddp(0, True, False, -1, -1)[1]

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.getSumWaviness(str(num2)) - self.getSumWaviness(str(num1 - 1))


s = Solution()
print(s.totalWaviness(num1=120, num2=130))
print(s.totalWaviness(num1=198, num2=202))
print(s.totalWaviness(num1=4848, num2=4848))

"""
3753. Total Waviness of Numbers in Range II
2827. Number of Beautiful Integers in the Range
2376. Count Special Integers
3490. Count Beautiful Numbers
2719. Count of Integers
2801. Count Stepping Numbers in Range
2999. Count the Number of Powerful Integers
3519. Count Numbers with Non-Decreasing Digits
3704. Count No-Zero Pairs That Sum to N
3869. Count Fancy Numbers in a Range
3646. Next Special Palindrome Number
"""
