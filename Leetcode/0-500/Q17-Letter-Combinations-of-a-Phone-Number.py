from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []
        res = []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        cur = []

        def dfs(i):
            if i == n:
                res.append("".join(cur))
                return
            for c in digit_to_letters[digits[i]]:
                cur.append(c)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
