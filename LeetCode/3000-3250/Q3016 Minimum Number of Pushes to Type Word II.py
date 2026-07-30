from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        pairs = []
        for c, f in freq.items():
            pairs.append([f, c])
        pairs.sort(reverse=True)
        res = 0
        presses = 1
        counter = 0
        for f, c in pairs:
            res += f * presses
            counter += 1
            if counter == 8:
                counter = 0
                presses += 1
        return res


s = Solution()
print(s.minimumPushes(word="abcde"))  # 5
print(s.minimumPushes(word="xyzxyzxyzxyz"))  # 12
print(s.minimumPushes(word="aabbccddeeffgghhiiiiii"))  # 24
