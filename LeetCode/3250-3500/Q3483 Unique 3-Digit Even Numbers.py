from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        res = 0
        seen = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if i == k or j == k or digits[k] & 1:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num not in seen:
                        res += 1
                        seen.add(num)
        return res


s = Solution()
print(s.totalNumbers([1, 2, 3, 4]))
print(s.totalNumbers([0, 2, 2]))
print(s.totalNumbers([6, 6, 6]))
print(s.totalNumbers([1, 3, 5]))
