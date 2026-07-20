class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = [0] * 26
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1
        st = []

        for c in s:
            idx = ord(c) - ord("a")
            if not seen[idx]:
                while st and st[-1] > c:
                    top_idx = ord(st[-1]) - ord("a")
                    if freq[top_idx] > 0:
                        seen[top_idx] = 0
                        st.pop()
                    else:
                        break
                seen[idx] = 1
                st.append(c)
            freq[idx] -= 1

        return "".join(st)


s = Solution()
print(s.smallestSubsequence(s="bcabc"))
print(s.smallestSubsequence(s="cbacdcbc"))
print(s.smallestSubsequence(s="cdadabcc"))
print(s.smallestSubsequence(s="leetcode"))
print(s.smallestSubsequence(s="bbbbaaaababaaabbbabbabaabaabbabaaaababbb"))
print(s.smallestSubsequence(s="edgebcbddfhafbcafbggbaadchcehhdaagfadedchbgbeadbde"))
