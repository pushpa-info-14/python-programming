import bisect
from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, arr)

    def _build(self, node, low, high, arr):
        if low == high:
            self.tree[node] = arr[low]
        else:
            mid = (low + high) // 2
            self._build(2 * node + 1, low, mid, arr)
            self._build(2 * node + 2, mid + 1, high, arr)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node, low, high, l, r):
        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return 0
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.tree[node]
        # Partial overlap
        mid = (low + high) // 2
        left = self._query(2 * node + 1, low, mid, l, r)
        right = self._query(2 * node + 2, mid + 1, high, l, r)
        return max(left, right)

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ones = 0
        zeros = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zeros.append([i, j - 1])
                i = j
            else:
                ones += 1
                i += 1
        if len(zeros) < 2:
            return [ones] * len(queries)

        pairs = []
        for i in range(1, len(zeros)):
            l1, r1 = zeros[i - 1]
            l2, r2 = zeros[i]
            pairs.append((r1 - l1 + 1) + (r2 - l2 + 1))

        st = SegmentTree(pairs)
        starts = [block[0] for block in zeros]
        ends = [block[1] for block in zeros]
        res = []
        for l, r in queries:
            first = bisect.bisect_left(ends, l)
            last = bisect.bisect_right(starts, r) - 1
            if first >= last:
                res.append(ones)
                continue
            best = st.query(first + 1, last - 2)

            # touching left
            prev_l = min(zeros[first][1], r) - max(zeros[first][0], l) + 1
            next_l = min(zeros[first + 1][1], r) - max(zeros[first + 1][0], l) + 1
            best = max(best, prev_l + next_l)

            # touching right
            prev_r = min(zeros[last - 1][1], r) - max(zeros[last - 1][0], l) + 1
            next_r = min(zeros[last][1], r) - max(zeros[last][0], l) + 1
            best = max(best, prev_r + next_r)

            res.append(ones + best)
        return res


s = Solution()
print(s.maxActiveSectionsAfterTrade(s="01", queries=[[0, 1]]))
print(s.maxActiveSectionsAfterTrade(s="0100", queries=[[0, 3], [0, 2], [1, 3], [2, 3]]))
print(s.maxActiveSectionsAfterTrade(s="1000100", queries=[[1, 5], [0, 6], [0, 4]]))
print(s.maxActiveSectionsAfterTrade(s="01010", queries=[[0, 3], [1, 4], [1, 3]]))
