class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # next_zero[i] = index of closest zero after position i
        # or n inf none exists
        next_zero = [n] * n
        for i in range(n - 2, -1, -1):
            if s[i + 1] == '0':
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]
        res = 0
        for l in range(n):
            zeros = 1 if s[l] == '0' else 0
            r = l
            while zeros * zeros <= n:
                # next_zero_idx is right boundary (non-inclusive)
                next_zero_idx = next_zero[r]
                ones = (next_zero_idx - l) - zeros
                if ones >= zeros * zeros:
                    res += min(next_zero_idx - r, ones - zeros * zeros + 1)
                r = next_zero_idx
                zeros += 1
                if r == n:
                    break
        return res


solution = Solution()
print(solution.numberOfSubstrings(s="00011"))
print(solution.numberOfSubstrings(s="101101"))
