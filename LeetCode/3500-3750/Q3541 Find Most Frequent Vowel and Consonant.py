from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_freq_vowels = 0
        max_freq_consonants = 0
        for c in set(s):
            if c in 'aeiou':
                max_freq_vowels = max(max_freq_vowels, s.count(c))
            else:
                max_freq_consonants = max(max_freq_consonants, s.count(c))
        return max_freq_vowels + max_freq_consonants

    def maxFreqSum2(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        max_freq_vowels = 0
        max_freq_consonants = 0
        for c in freq.keys():
            if c in 'aeiou':
                max_freq_vowels = max(max_freq_vowels, freq[c])
            else:
                max_freq_consonants = max(max_freq_consonants, freq[c])
        return max_freq_vowels + max_freq_consonants


s = Solution()
print(s.maxFreqSum(s="successes"))
print(s.maxFreqSum(s="aeiaeia"))
print(s.maxFreqSum2(s="successes"))
print(s.maxFreqSum2(s="aeiaeia"))
