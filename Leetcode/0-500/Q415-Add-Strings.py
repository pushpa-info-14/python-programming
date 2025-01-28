class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            num1 = "0" * (n2 - n1) + num1
        else:
            num2 = "0" * (n1 - n2) + num2

        carry = 0
        res = ""
        for i in reversed(range(len(num1))):
            total = int(num1[i]) + int(num2[i]) + carry
            carry = total // 10
            res = str(total % 10) + res

        if carry == 0:
            return res
        else:
            return str(carry) + res


s = Solution()
print(s.addStrings("11", "123"))
print(s.addStrings("456", "77"))
print(s.addStrings("0", "0"))
