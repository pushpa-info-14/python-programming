class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def build(s):
            parts = set()
            cur = {""}
            i = 0
            while i < len(s):
                if s[i] == '{':
                    j = i
                    depth = 0
                    while True:
                        if s[j] == '{':
                            depth -= 1
                        elif s[j] == '}':
                            depth += 1
                        if depth == 0:
                            break
                        j += 1
                    options = build(s[i + 1:j])
                    cur = {a + b for a in cur for b in options}
                    i = j + 1
                elif s[i] == ',':
                    parts |= cur
                    cur = {""}
                    i += 1
                else:
                    cur = {x + s[i] for x in cur}
                    i += 1
            parts |= cur
            return parts

        return sorted(build(expression))


s = Solution()
print(s.braceExpansionII(expression="{a,b}{c,{d,e}}"))
print(s.braceExpansionII(expression="{{a,z},a{b,c},{ab,z}}"))
