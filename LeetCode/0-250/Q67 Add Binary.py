class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        res = [""] * n
        num1 = "0" * (n - len(a)) + a
        num2 = "0" * (n - len(b)) + b
        carry = 0
        for i in reversed(range(n)):
            s = int(num1[i]) + int(num2[i]) + carry
            carry = s // 2
            res[i] = str(s % 2)
        if carry:
            return "1" + "".join(res)
        return "".join(res)


s = Solution()
print(s.addBinary(a="11", b="1"))
print(s.addBinary(a="1010", b="1011"))
