class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        st = [-1]
        res = 0
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if len(st) > 0:
                    res = max(res, i - st[-1])
                else:
                    st.append(i)
        return res


s = Solution()
print(s.longestValidParentheses(s="(()"))
print(s.longestValidParentheses(s=")()())"))
print(s.longestValidParentheses(s=""))
print(s.longestValidParentheses(s="()"))
