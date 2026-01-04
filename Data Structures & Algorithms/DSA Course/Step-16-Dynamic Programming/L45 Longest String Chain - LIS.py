from typing import List


def check(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    if n1 + 1 != n2:
        return False

    i, j = 0, 0
    while j < n2:
        if i < n1 and word1[i] == word2[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == n1 and j == n2:
        return True
    return False


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x))
        dp = [1] * n
        res = 1

        for i in range(1, n):
            for prev in range(i):
                if check(words[prev], words[i]):
                    dp[i] = max(dp[i], 1 + dp[prev])
            res = max(res, dp[i])
        return res

    def longestStrChain2(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    res = max(res, dp[word])
        return res


# LeetCode 1048
s = Solution()
print(s.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]))
print(s.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(s.longestStrChain(words=["abcd", "dbqca"]))
print("-----------------")
print(s.longestStrChain2(words=["a", "b", "ba", "bca", "bda", "bdca"]))
print(s.longestStrChain2(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(s.longestStrChain2(words=["abcd", "dbqca"]))
