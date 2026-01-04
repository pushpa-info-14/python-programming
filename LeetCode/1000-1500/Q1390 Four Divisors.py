from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisors = []
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisors.append(i)
                    if num // i != i:
                        divisors.append(num // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                res += sum(divisors)
        return res


s = Solution()
print(s.sumFourDivisors(nums=[21, 4, 7]))
print(s.sumFourDivisors(nums=[21, 21]))
print(s.sumFourDivisors(nums=[1, 2, 3, 4, 5]))
