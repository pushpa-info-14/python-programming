class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        total = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i
                if num // i != i:
                    total += num // i
        return total == num


s = Solution()
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(7))
print(s.checkPerfectNumber(99999996))
print(s.checkPerfectNumber(1))
