def get_num(s):
    res = 0
    for c in s:
        res += ord(c) - ord('a')
        res *= 10
    return res


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        x = get_num(firstWord)
        y = get_num(secondWord)
        z = get_num(targetWord)
        return x + y == z


s = Solution()
print(s.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa"))
