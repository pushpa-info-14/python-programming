from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, v, tl, tr, l, r, val):
        if tl > r or tr < l:
            return
        if l <= tl and tr <= r:
            self.tree[v] = max(self.tree[v], val)
            return
        mid = (tl + tr) // 2
        self.update(2 * v, tl, mid, l, r, val)
        self.update(2 * v + 1, mid + 1, tr, l, r, val)

    def query(self, v, tl, tr, index):
        if tl > index or tr < index:
            return 0
        if tl == tr:
            return self.tree[v]
        mid = (tl + tr) // 2

        if index <= mid:
            return max(self.tree[v], self.query(2 * v, tl, mid, index))
        else:
            return max(self.tree[v], self.query(2 * v + 1, mid + 1, tr, index))


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = sorted(set([x for b in buildings for x in (b[0], b[1])]))
        index = {x: i for i, x in enumerate(points)}

        tree = SegmentTree(len(points))
        for L, R, H in buildings:
            tree.update(1, 0, len(points) - 1, index[L], index[R] - 1, H)

        result, prev_height = [], 0
        for x in points:
            height = tree.query(1, 0, len(points) - 1, index[x])
            if height != prev_height:
                result.append([x, height])
                prev_height = height

        return result


s = Solution()
print(s.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
print(s.getSkyline(buildings=[[0, 2147483647, 2147483647]]))
