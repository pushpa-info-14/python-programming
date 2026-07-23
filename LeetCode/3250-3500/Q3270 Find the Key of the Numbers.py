def get_digits(x):
    res = [0, 0, 0, 0]
    i = 3
    while x:
        res[i] = x % 10
        i -= 1
        x //= 10
    return res


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = 0
        digits1 = get_digits(num1)
        digits2 = get_digits(num2)
        digits3 = get_digits(num3)
        for i in range(4):
            key *= 10
            key += min(digits1[i], digits2[i], digits3[i])
        return key


s = Solution()
print(s.generateKey(num1=1, num2=10, num3=1000))
print(s.generateKey(num1=987, num2=879, num3=798))
print(s.generateKey(num1=1, num2=2, num3=3))
print(s.generateKey(num1=282, num2=718, num3=1028))
