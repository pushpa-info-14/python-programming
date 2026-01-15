from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self._build(arr, left, start, mid)
            self._build(arr, right, mid + 1, end)
            self.tree[node] = self.tree[left] + self.tree[right]

    def _query(self, node, start, end, l, r):
        # No overlap [l r start end] [start end l r]
        if r < start or end < l:
            return 0
        # Complete overlap [l start end r]
        if l <= start and end <= r:
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        return (
                self._query(2 * node + 1, start, mid, l, r) +
                self._query(2 * node + 2, mid + 1, end, l, r)
        )

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node + 1, start, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, end, index, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)


class Solution:
    def inversionCount(self, nums: List[int]) -> int:
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        st = SegmentTree(freq)
        res = 0
        for num in nums:
            freq[num] -= 1
            st.update(num, freq[num])
            res += st.query(1, num - 1)
        return res


s = Solution()
print(s.inversionCount([5, 3, 2, 4, 1]))  # 8
print(s.inversionCount([6, 4, 5, 3, 1, 2]))  # 13
