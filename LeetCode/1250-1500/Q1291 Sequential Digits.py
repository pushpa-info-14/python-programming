from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        n1 = len(str(low))
        n2 = len(str(high))
        res = []
        for i in range(n1, n2 + 1):
            l, r = 0, i
            while r <= 9:
                num = int(digits[l: r])
                if low <= num <= high:
                    res.append(num)
                l += 1
                r += 1
        return res


s = Solution()
print(s.sequentialDigits(low=100, high=300))
print(s.sequentialDigits(low=1000, high=13000))
