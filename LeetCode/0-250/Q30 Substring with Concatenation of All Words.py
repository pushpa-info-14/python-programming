from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        word_length = len(words[0])
        window_length = word_length * len(words)
        res = []
        for i in range(word_length):
            start = i

            while start + window_length - 1 < n:
                match_found = True
                cur = freq.copy()
                for j in range(start, start + window_length, word_length):
                    w = s[j: j + word_length]
                    if w in cur and cur[w] != 0:
                        cur[w] -= 1
                    else:
                        match_found = False
                        break
                if match_found:
                    res.append(start)
                start += word_length

        return res


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # [0, 9]
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # []
print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6, 9, 12]
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))  # [8]
