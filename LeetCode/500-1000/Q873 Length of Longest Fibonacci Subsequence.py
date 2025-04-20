from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        mp = set(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                while nxt in mp:
                    length += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    res = max(res, length)
        return res

    def lenLongestFibSubseq2(self, arr: List[int]) -> int:
        n = len(arr)
        arr_map = {num: i for i, num in enumerate(arr)}
        res = 0
        dp = [[0] * n for _ in range(n)]  # [i][j] -> length of longest subseq
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                    res = max(res, length)
                dp[i][j] = length
        return res


s = Solution()
print(s.lenLongestFibSubseq([1, 3, 5]))
print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
print(s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
print(s.lenLongestFibSubseq([1, 3, 4, 7, 10, 11, 12, 18, 23, 35]))

print(s.lenLongestFibSubseq2([1, 3, 5]))
print(s.lenLongestFibSubseq2([1, 2, 3, 4, 5, 6, 7, 8]))
print(s.lenLongestFibSubseq2([1, 3, 7, 11, 12, 14, 18]))
print(s.lenLongestFibSubseq2([1, 3, 4, 7, 10, 11, 12, 18, 23, 35]))
