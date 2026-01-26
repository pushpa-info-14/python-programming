from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowels = set(list("aeiou"))
        res = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                if word[j] in vowels:
                    freq[word[j]] += 1
                else:
                    break
                if len(freq) == 5:
                    res += 1
        return res


s = Solution()
print(s.countVowelSubstrings(word="aeiouu"))
print(s.countVowelSubstrings(word="unicornarihan"))
print(s.countVowelSubstrings(word="cuaieuouac"))
