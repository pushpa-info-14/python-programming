import bisect

good_integers = []
for num in range(1, 10001):
    x = num
    flag = False
    while x:
        digit = x % 10
        if digit in [3, 4, 7]:
            flag = False
            break
        if digit in [2, 5, 6, 9]:
            flag = True
        x //= 10
    if flag:
        good_integers.append(num)


class Solution:
    def rotatedDigits(self, n: int) -> int:
        return bisect.bisect_left(good_integers, n + 1)


s = Solution()
print(s.rotatedDigits(10))
print(s.rotatedDigits(1))
print(s.rotatedDigits(2))
