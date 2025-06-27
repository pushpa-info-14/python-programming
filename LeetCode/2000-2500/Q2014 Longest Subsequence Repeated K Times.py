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
        q = deque([''])
        res = ''
        while q:
            cur_seq = q.popleft()
            for c in valid_characters:
                next_seq = cur_seq + c
                if count_subsequence(next_seq, s) >= k:
                    res = next_seq
                    q.append(next_seq)
        return res


s = Solution()
print(s.longestSubsequenceRepeatedK(s="letsleetcode", k=2))
print(s.longestSubsequenceRepeatedK(s="bb", k=2))
print(s.longestSubsequenceRepeatedK(s="ab", k=2))
