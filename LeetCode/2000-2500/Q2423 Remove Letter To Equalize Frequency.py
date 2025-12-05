from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for c in list(counter.keys()):
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
            if len(set(counter.values())) == 1:
                return True
            counter[c] += 1
        return False


s = Solution()
print(s.equalFrequency(word="abcc"))
print(s.equalFrequency(word="aazz"))
print(s.equalFrequency(word="bac"))
print(s.equalFrequency(word="ddaccb"))
print(s.equalFrequency(word="aca"))
