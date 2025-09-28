from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        original = set(wordlist)
        capitalized = {}
        replaced = {}

        def vowel_key(s):
            l = list(s)
            for idx, c in enumerate(l):
                if c in "aeiou":
                    l[idx] = '*'
            return ''.join(l)

        for word in wordlist:
            lower = word.lower()

            if lower not in capitalized:
                capitalized[lower] = word

            replaced_key = vowel_key(lower)
            if replaced_key not in replaced:
                replaced[replaced_key] = word

        res = []
        for word in queries:
            if word in original:
                res.append(word)
                continue
            lower = word.lower()
            if lower in capitalized:
                res.append(capitalized[lower])
                continue
            replaced_key = vowel_key(lower)
            if replaced_key in replaced:
                res.append(replaced[replaced_key])
                continue
            res.append('')
        return res


s = Solution()
print(s.spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"],
                     queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
print(s.spellchecker(wordlist=["yellow"], queries=["YellOw"]))
