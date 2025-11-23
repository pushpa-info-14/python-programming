class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"

        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        res = ""

        if num < 0:
            num = pow(2, 32) + num
        while num:
            rem = num % 16
            num = num // 16
            res = digits[rem] + res

        return res


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))
print(s.toHex(-2))
