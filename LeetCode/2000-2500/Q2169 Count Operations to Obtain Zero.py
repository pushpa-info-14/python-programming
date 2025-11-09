class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 and num2:
            if num1 > num2:
                res += num1 // num2
                num1 %= num2
            else:
                res += num2 // num1
                num2 %= num1
        return res


s = Solution()
print(s.countOperations(num1=2, num2=3))
print(s.countOperations(num1=10, num2=10))
