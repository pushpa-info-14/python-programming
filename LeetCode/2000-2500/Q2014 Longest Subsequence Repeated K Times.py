from collections import Counter, deque


def count_subsequence(sequence, s):
    j = 0
    count = 0
    for i in range(len(s)):
        if sequence[j] == s[i]:
            j += 1
        if j == len(sequence):
            j = 0
            count += 1
    return count


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid_characters = []
        for char in freq.keys():
            if freq[char] >= k:
                valid_characters.append(char)

        valid_characters.sort()
        q = deque(valid_characters)
        res = ''
        while q:
            cur = q.popleft()
            res = cur
            for c in valid_characters:
                if count_subsequence(cur + c, s) >= k:
                    q.append(cur + c)
        return res


s = Solution()
print(s.longestSubsequenceRepeatedK(s="letsleetcode", k=2))
print(s.longestSubsequenceRepeatedK(s="bb", k=2))
print(s.longestSubsequenceRepeatedK(s="ab", k=2))
