from collections import defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        for i in range(t):
            new_freq = defaultdict(int)
            for c in freq.keys():
                if c == 'z':
                    new_freq['a'] += freq[c] % mod
                    new_freq['b'] += freq[c] % mod
                else:
                    new_freq[chr(ord(c) + 1)] += freq[c] % mod
            freq = new_freq

        return sum(freq.values()) % mod

    def lengthAfterTransformations2(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord("a")] += 1

        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = count[25]
            nxt[1] = (count[25] + count[0]) % mod
            for i in range(2, 26):
                nxt[i] = count[i - 1]
            count = nxt
        ans = sum(count) % mod

        return ans


s = Solution()
print(s.lengthAfterTransformations("abcyy", 2))  # 7
print(s.lengthAfterTransformations("azbk", 1))  # 5
print(s.lengthAfterTransformations2("abcyy", 2))  # 7
print(s.lengthAfterTransformations2("azbk", 1))  # 5
