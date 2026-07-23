class Solution:
    def minMaxDifference(self, num: int) -> int:
        cur = num
        digits = []
        while cur:
            digits.append(cur % 10)
            cur //= 10

        n = len(digits)
        digits = digits[::-1]
        mini = digits.copy()
        maxi = digits.copy()

        for i in range(n):
            if mini[i] == digits[0]:
                mini[i] = 0

        for i in range(n):
            if maxi[i] != 9:
                for j in range(i, n):
                    if maxi[j] == digits[i]:
                        maxi[j] = 9
                break

        min_number = 0
        max_number = 0
        for i in range(n):
            min_number += mini[i] * (10 ** (n - i - 1))
            max_number += maxi[i] * (10 ** (n - i - 1))

        return max_number - min_number


s = Solution()
print(s.minMaxDifference(11891))
print(s.minMaxDifference(90))
