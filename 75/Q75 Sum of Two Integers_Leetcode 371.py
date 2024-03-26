class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(num1, num2):
            while num2 != 0:
                temp = num1 ^ num2
                num2 = (num1 & num2) << 1
                num1 = temp
            return num1

        def sub(num1, num2, flip=False):
            while num2 != 0:
                temp = num1 ^ num2
                num2 = (~num1 & num2) << 1
                num1 = temp
            return num1 if not flip else -num1

        if a >= 0 and b >= 0:
            return add(a, b)
        elif a < 0 and b < 0:
            return -add(-a, -b)
        else:
            maxVal = max(a, b)
            minVal = min(a, b)
            return sub(max(maxVal, -minVal), min(maxVal, -minVal), True if -minVal > maxVal else False)


solution = Solution()
print(solution.getSum(1, 2))
print(solution.getSum(-1, -2))
print(solution.getSum(-1, 2))
print(solution.getSum(-2, 2))
print(solution.getSum(-2, 1))
