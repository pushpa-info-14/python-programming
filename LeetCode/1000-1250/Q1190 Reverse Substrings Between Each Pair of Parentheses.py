class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for c in s:
            if c != ')':
                st.append(c)
            else:
                cur = []
                while st[-1] != '(':
                    cur.append(st.pop())
                st.pop()
                st += cur
        return ''.join(st)


s = Solution()
print(s.reverseParentheses(s="(abcd)"))
print(s.reverseParentheses(s="(u(love)i)"))
print(s.reverseParentheses(s="(ed(et(oc))el)"))
