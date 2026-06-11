import heapq
from typing import List


class SegmentTree:
    inf = 10 ** 10

    def __init__(self, arr):
        self.n = len(arr)
        self.min = [0] * (4 * self.n)
        self.max = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, arr)

    def _build(self, node, low, high, arr):
        if low == high:
            self.min[node] = arr[low]
            self.max[node] = arr[low]
        else:
            mid = (low + high) // 2
            self._build(2 * node + 1, low, mid, arr)
            self._build(2 * node + 2, mid + 1, high, arr)
            self.min[node] = min(self.min[2 * node + 1], self.min[2 * node + 2])
            self.max[node] = max(self.max[2 * node + 1], self.max[2 * node + 2])

    def _query(self, node, low, high, l, r):
        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return self.inf, -self.inf
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            return self.min[node], self.max[node]
        # Partial overlap
        mid = (low + high) // 2
        l_min, l_max = self._query(2 * node + 1, low, mid, l, r)
        r_min, r_max = self._query(2 * node + 2, mid + 1, high, l, r)
        return min(l_min, r_min), max(l_max, r_max)

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SegmentTree(nums)
        mn, mx = st.query(0, n - 1)
        q = [(mn - mx, 0, n - 1)]
        seen = set()
        res = 0
        while q:
            value, l, r = heapq.heappop(q)
            value = -value
            res += value
            k -= 1
            if k == 0:
                break
            if r - l > 1:
                if (l, r - 1) not in seen:
                    mn, mx = st.query(l, r - 1)
                    heapq.heappush(q, (mn - mx, l, r - 1))
                    seen.add((l, r - 1))
                if (l + 1, r) not in seen:
                    mn, mx = st.query(l + 1, r)
                    heapq.heappush(q, (mn - mx, l + 1, r))
                    seen.add((l + 1, r))
        return res


s = Solution()
print(s.maxTotalValue(nums=[1, 3, 2], k=2))
print(s.maxTotalValue(nums=[4, 2, 5, 1], k=3))
