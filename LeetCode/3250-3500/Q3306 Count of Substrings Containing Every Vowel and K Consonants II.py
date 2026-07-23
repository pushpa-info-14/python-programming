from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atLeastK(k):
            vowels = "aeiou"
            consonants = 0
            freq = defaultdict(int)
            res = 0
            l = 0
            for r in range(n):
                if word[r] in vowels:
                    freq[word[r]] += 1
                else:
                    consonants += 1

                while len(freq) == 5 and consonants >= k:
                    res += n - r
                    if word[l] in vowels:
                        freq[word[l]] -= 1
                        if freq[word[l]] == 0:
                            del freq[word[l]]
                    else:
                        consonants -= 1
                    l += 1
            return res

        return atLeastK(k) - atLeastK(k + 1)


s = Solution()
print(s.countOfSubstrings(word="aeioqq", k=1))
print(s.countOfSubstrings(word="aeiou", k=0))
print(s.countOfSubstrings(word="ieaouqqieaouqq", k=1))
print(s.countOfSubstrings(word="iqeaouqi", k=2))
