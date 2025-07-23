class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def process(pattern, chars, points):
            total = 0
            stack = []
            for c in chars:
                if c == pattern[1] and stack and stack[-1] == pattern[0]:
                    stack.pop()
                    total += points
                else:
                    stack.append(c)
            chars[:] = stack
            return total

        res = 0
        copy_s = list(s)
        if x > y:
            res += process('ab', copy_s, x)
            res += process('ba', copy_s, y)
        else:
            res += process('ba', copy_s, y)
            res += process('ab', copy_s, x)
        return res


solution = Solution()
print(solution.maximumGain(s="cdbcbbaaabab", x=4, y=5))
print(solution.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
