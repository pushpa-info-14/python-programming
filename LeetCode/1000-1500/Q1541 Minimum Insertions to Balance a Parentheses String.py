class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', 'x')
        res = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                if count:
                    count -= 1
                else:
                    res += 1
                if c == ')':
                    res += 1
        return res + count * 2


s = Solution()
print(s.minInsertions(s="(()))"))
print(s.minInsertions(s="())"))
print(s.minInsertions(s="))())("))
print(s.minInsertions(s=")))))))"))  # 5
print(s.minInsertions(s="(()))(()))()())))"))  # 4
