from typing import List


class Node:
    def __init__(self, val=0):
        self.val = val

    def merge(self, l, r):
        self.val = l.val + r.val


class Update:
    def __init__(self, val=0):
        self.val = val

    def combine(self, other_update):
        self.val += other_update.val

    def apply(self, node: Node, tl: int, tr: int):
        node.val = (tr - tl + 1) * self.val


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [Node() for _ in range(4 * size + 1)]
        self.isLazy = [False] * (4 * size + 1)
        self.pendingUpdates = [Update() for _ in range(4 * size + 1)]
        self.identityElement = Node()
        self.identityTransformation = Update()

    def _build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = Node(arr[tl])
            return

        tm = (tl + tr) // 2
        self._build(arr, 2 * v, tl, tm)
        self._build(arr, 2 * v + 1, tm + 1, tr)
        self.tree[v].merge(self.tree[2 * v], self.tree[2 * v + 1])

    def _query(self, v, tl, tr, l, r):
        if tr < l or tl > r:  # No overlap
            return self.identityElement
        if l <= tl and tr <= r:  # Full overlap
            return self.tree[v]

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        left_ans = self._query(2 * v, tl, tm, l, r)
        right_ans = self._query(2 * v + 1, tm + 1, tr, l, r)
        ans = Node()
        ans.merge(left_ans, right_ans)
        return ans

    def _update(self, v: int, tl: int, tr: int, l: int, r: int, update: Update):
        if r < tl or tr < l:  # No overlap
            return
        if l <= tl and tr <= r:  # Full overlap
            self._apply(v, tl, tr, update)
            return

        # Partial overlap
        self._pushDown(v, tl, tr)
        tm = (tl + tr) // 2
        self._update(2 * v, tl, tm, l, r, update)
        self._update(2 * v + 1, tm + 1, tr, l, r, update)
        self.tree[v].merge(self.tree[2 * v], self.tree[2 * v + 1])

    def _pushDown(self, v, tl, tr):
        if not self.isLazy[v]:
            return
        self.isLazy[v] = False
        tm = (tl + tr) // 2
        self._apply(2 * v, tl, tm, self.pendingUpdates[v])
        self._apply(2 * v + 1, tm + 1, tr, self.pendingUpdates[v])
        self.pendingUpdates[v].val = self.identityTransformation.val

    def _apply(self, v: int, tl: int, tr: int, update: Update):
        if tl != tr:  # Leaf nodes can't be lazy
            self.isLazy[v] = True
            self.pendingUpdates[v].combine(update)
        update.apply(self.tree[v], tl, tr)

    def build(self, arr):
        self._build(arr, 1, 0, self.size - 1)

    def query(self, l: int, r: int):
        return self._query(1, 0, self.size - 1, l, r)

    def update(self, l: int, r: int, update: Update):
        self._update(1, 0, self.size - 1, l, r, update)


def isPeak(nums, index):
    if 0 <= index and index + 1 < len(nums) and nums[index - 1] < nums[index] > nums[index + 1]:
        return True
    return False


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(n)
        for i in range(1, n - 1):
            if isPeak(nums, i):
                st.update(i, i, Update(1))

        res = []
        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                if r - l < 2:  # At least 3 elements should exist to have a peak
                    res.append(0)
                else:
                    res.append(st.query(l + 1, r - 1).val)
            else:
                index, val = query[1], query[2]
                prv = index - 1
                nxt = index + 1
                nums[index] = val

                if isPeak(nums, prv):
                    st.update(prv, prv, Update(1))
                else:
                    st.update(prv, prv, Update(0))
                if isPeak(nums, index):
                    st.update(index, index, Update(1))
                else:
                    st.update(index, index, Update(0))
                if isPeak(nums, nxt):
                    st.update(nxt, nxt, Update(1))
                else:
                    st.update(nxt, nxt, Update(0))

        return res


s = Solution()
print(s.countOfPeaks(nums=[3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]]))
print(s.countOfPeaks(nums=[4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]]))
print(s.countOfPeaks(nums=[7, 10, 7], queries=[[1, 2, 2], [2, 0, 6], [1, 0, 2]]))
print(s.countOfPeaks(nums=[9, 7, 5, 8, 9], queries=[[2, 0, 2], [1, 0, 3], [1, 3, 3], [2, 3, 5]]))
