class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if st and st[-1] == '(' and c == ')':
                st.pop()
            else:
                st.append(c)
        return len(st)

s = Solution()
print(s.minAddToMakeValid(s = "())"))
print(s.minAddToMakeValid(s = "((("))