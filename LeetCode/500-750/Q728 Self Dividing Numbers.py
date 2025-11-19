from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            x = num
            is_valid = True
            while x:
                digit = x % 10
                if digit == 0 or num % digit:
                    is_valid = False
                    break
                x //= 10
            if is_valid:
                res.append(num)
        return res


s = Solution()
print(s.selfDividingNumbers(left=1, right=22))
print(s.selfDividingNumbers(left=47, right=85))
