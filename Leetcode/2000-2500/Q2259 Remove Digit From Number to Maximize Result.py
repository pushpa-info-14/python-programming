class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        to_remove = -1

        for i in range(n):
            if number[i] == digit:
                to_remove = i
                if i < n - 1 and to_remove != -1 and number[to_remove] < number[to_remove + 1]:
                    break

        return number[:to_remove] + number[to_remove + 1:]


s = Solution()
print(s.removeDigit("123", "3"))
print(s.removeDigit("1231", "1"))
