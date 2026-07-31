from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = list(Counter(word).values())
        freq.sort(reverse=True)
        res = 0
        presses = 1
        counter = 0
        for f in freq:
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
