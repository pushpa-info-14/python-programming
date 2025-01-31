class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        index = 0
        while index < n and s[index] == " ":
            index += 1

        if index == n: return 0

        sign = 1
        if s[index] == "+" or s[index] == "-":
            sign = 1 if s[index] == "+" else -1
            index += 1

        int_max = 2 ** 31 - 1
        res = 0
        while index < n:
            digit = ord(s[index]) - ord("0")
            if digit < 0 or digit > 9: break

            res = res * 10 + digit
            if int_max < res:
                return int_max if sign == 1 else -int_max - 1
            index += 1

        return res * sign


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi(" -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("+-12"))
print(s.myAtoi("21474836460"))
print(s.myAtoi(" "))
print(s.myAtoi("2147483648"))
