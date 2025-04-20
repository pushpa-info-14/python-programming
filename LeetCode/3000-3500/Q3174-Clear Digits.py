from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        delete_count = 0

        for i in reversed(range(len(s))):
            if s[i].isnumeric():
                delete_count += 1
            else:
                if delete_count > 0:
                    delete_count -= 1
                else:
                    res = s[i] + res
        return res

    def clearDigits2(self, s: str) -> str:
        res = ""
        stack = deque()

        for i in range(len(s)):
            if s[i].isnumeric():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


s = Solution()
print(s.clearDigits("abc"))
print(s.clearDigits("cb34"))

print(s.clearDigits2("abc"))
print(s.clearDigits2("cb34"))
