def get_digits(num):
    digits = []
    while num:
        digits.append(num % 10)
        num //= 10
    return digits[::-1]


def get_number(digits):
    n = len(digits)
    num = 0
    for i in range(n):
        num += digits[i] * 10 ** (n - i - 1)
    return num


class Solution:
    def maxDiff(self, num: int) -> int:
        digits = get_digits(num)
        max_digits = digits.copy()
        min_digits = digits.copy()
        n = len(digits)

        x = digits[0]
        for i in range(n):
            if max_digits[i] != 9:
                x = max_digits[i]
                break
        for i in range(n):
            if max_digits[i] == x:
                max_digits[i] = 9

        x = digits[0]
        y = 1
        if 1 == min_digits[0]:
            for i in range(1, n):
                if min_digits[i] != 1 and min_digits[i] != 0:
                    x = min_digits[i]
                    y = 0
                    break
        for i in range(n):
            if min_digits[i] == x:
                min_digits[i] = y

        max_number = get_number(max_digits)
        min_number = get_number(min_digits)
        # print(max_number, min_number)
        return max_number - min_number


s = Solution()
print(s.maxDiff(555))
print(s.maxDiff(9))
print(s.maxDiff(123456))  # 820000
print(s.maxDiff(9288))  # 8700
print(s.maxDiff(1101057))  # 8808050
