from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(map(int, num))
        for i in range(len(num)):
            if counter[i] != int(num[i]):
                return False
        return True


s = Solution()
print(s.digitCount(num="1210"))
print(s.digitCount(num="030"))
