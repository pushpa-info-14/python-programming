from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        min_character = "a"
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while min_character != "z" and cnt[min_character] == 0:
                min_character = chr(ord(min_character) + 1)
            while stack and stack[-1] <= min_character:
                res.append(stack.pop())
        return "".join(res)


s = Solution()
print(s.robotWithString("zza"))
print(s.robotWithString("bac"))
print(s.robotWithString("bdda"))
