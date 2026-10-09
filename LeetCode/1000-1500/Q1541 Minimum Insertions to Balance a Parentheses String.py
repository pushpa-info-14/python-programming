class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', 'x')
        res = 0
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st:
                    st.pop()
                else:
                    res += 1
                if c == ')':
                    res += 1
        return res + len(st) * 2


s = Solution()
print(s.minInsertions(s="(()))"))
print(s.minInsertions(s="())"))
print(s.minInsertions(s="))())("))
print(s.minInsertions(s=")))))))"))  # 5
print(s.minInsertions(s="(()))(()))()())))"))  # 4
