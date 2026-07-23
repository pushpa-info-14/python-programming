from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = Counter("balloon")
        counter = Counter(text)
        res = len(text)
        for c in word.keys():
            res = min(res, counter[c] // word[c])
        return res


s = Solution()
print(s.maxNumberOfBalloons(text="nlaebolko"))
print(s.maxNumberOfBalloons(text="loonbalxballpoon"))
print(s.maxNumberOfBalloons(text="leetcode"))
