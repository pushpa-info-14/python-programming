class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        flag = True
        for i in range(0, n, k):
            if flag:
                res += s[i: i + k][::-1]
            else:
                res += s[i:i + k]
            flag = not flag
        return res


s = Solution()
print(s.reverseStr(s="abcdefg", k=2))
print(s.reverseStr(s="abcdefgh", k=3))
print(s.reverseStr(s="abcd", k=2))
