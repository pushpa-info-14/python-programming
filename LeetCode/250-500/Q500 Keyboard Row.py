from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mp = {}
        for c in "qwertyuiop":
            mp[c] = 1
        for c in "asdfghjkl":
            mp[c] = 2
        for c in "zxcvbnm":
            mp[c] = 3
        res = []
        for word in words:
            lower_word = word.lower()
            row = mp[lower_word[0]]
            flag = True
            for c in lower_word[1:]:
                if mp[c] != row:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res


s = Solution()
print(s.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
print(s.findWords(words=["omk"]))
print(s.findWords(words=["adsdf", "sfd"]))
