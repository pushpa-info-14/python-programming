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
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

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
        return left + right

    def _update(self, node, low, high, index, val):
        if low == high:
            self.tree[node] += val
        else:
            mid = (low + high) // 2
            if index <= mid:
                self._update(2 * node + 1, low, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, high, index, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)


class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        mp = {}
        unique_nums = sorted(list(set(nums)))
        for i in range(len(unique_nums)):
            mp[unique_nums[i]] = i + 1  # Mapping all the numbers to 1 - n
        n = len(unique_nums)
        arr = [0] * (n + 1)
        st = SegmentTree(arr)

        res = 10 ** 10
        count = 0
        l = 0
        for r in range(len(nums)):
            st.update(mp[nums[r]], 1)
            count += st.query(mp[nums[r]] + 1, n)
            if r - l + 1 == k:
                res = min(res, count)
                st.update(mp[nums[l]], -1)
                count -= st.query(0, mp[nums[l]] - 1)
                l += 1
        return res


s = Solution()
print(s.minInversionCount(nums=[3, 1, 2, 5, 4], k=3))
print(s.minInversionCount(nums=[5, 3, 2, 1], k=4))
print(s.minInversionCount(nums=[2, 1], k=1))
