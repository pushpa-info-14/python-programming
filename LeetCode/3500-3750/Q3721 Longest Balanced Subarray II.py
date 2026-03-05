from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.minimum = [0] * (4 * self.n)
        self.maximum = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

    def _push(self, node, low, high):
        if self.lazy[node] != 0:
            self.minimum[node] += self.lazy[node]
            self.maximum[node] += self.lazy[node]
            if low != high:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

    def _left_zero(self, node, low, high, l, r):
        self._push(node, low, high)

        if self.minimum[node] > 0 or self.maximum[node] < 0:
            return -1

        if low == high:  # Leaf
            if self.minimum[node] == 0:
                return low
            else:
                return -1

        mid = (low + high) // 2
        left = self._left_zero(node * 2 + 1, low, mid, l, r)
        if left != -1:
            return left
        right = self._left_zero(node * 2 + 2, mid + 1, high, l, r)
        return right

    def _update(self, node, low, high, l, r, val):
        self._push(node, low, high)

        # No overlap [l r low high] [low high l r]
        if r < low or high < l:
            return
        # Complete overlap [l low high r]
        if l <= low and high <= r:
            self.lazy[node] += val
            self._push(node, low, high)
            return
        # Partial overlap
        mid = (low + high) // 2
        self._update(node * 2 + 1, low, mid, l, r, val)
        self._update(node * 2 + 2, mid + 1, high, l, r, val)
        self.minimum[node] = min(self.minimum[node * 2 + 1], self.minimum[node * 2 + 2])
        self.maximum[node] = max(self.maximum[node * 2 + 1], self.maximum[node * 2 + 2])

    def left_zero(self, l, r):
        return self._left_zero(0, 0, self.n - 1, l, r)

    def update(self, l, r, val):
        self._update(0, 0, self.n - 1, l, r, val)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = {}
        st = SegmentTree(n)
        for r in range(n):
            cur = nums[r]
            val = 1 if cur % 2 == 0 else -1
            if cur in prev:
                st.update(0, prev[cur], -val)
            st.update(0, r, val)
            prev[cur] = r

            l = st.left_zero(0, n - 1)
            if l != -1:
                res = max(res, r - l + 1)
        return res


s = Solution()
print(s.longestBalanced(nums=[2, 5, 4, 3]))
print(s.longestBalanced(nums=[3, 2, 2, 5, 4]))
print(s.longestBalanced(nums=[1, 2, 3, 2]))
