from collections import defaultdict
from typing import List


class FenwickTree:
    def __init__(self, n):
        self.tree = [-1] * (n + 1)

    def update(self, index, x):
        index += 1
        while index < len(self.tree):
            self.tree[index] = max(x, self.tree[index])
            index += (index & -index)

    def query(self, index):
        index += 1
        ans = -1
        while index > 0:
            ans = max(ans, self.tree[index])
            index -= (index & -index)
        return ans


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums1)
        q = len(queries)
        res = [-1] * q

        # Coordinate compression
        # 1, 100000, 5, 62131, 9
        # 1, 5, 2, 4, 3
        ys = []
        for y in nums2:
            ys.append(y)
        for _, y in queries:
            ys.append(y)
        ys = list(set(ys))
        ys.sort(reverse=True)
        yl = {y: index for index, y in enumerate(ys)}

        ft = FenwickTree(len(ys) + 1)

        offline_queries = list(
            (x, y, index) for index, (x, y) in sorted(enumerate(queries), key=lambda v: (-v[1][0], v[1][1])))
        # print(offline_queries)

        np = defaultdict(list)
        for x, y in zip(nums1, nums2):
            np[x].append((0, yl[y], x + y))
        for x, y, index in offline_queries:
            np[x].append((1, yl[y], index))

        for k in sorted(np.keys(), reverse=True):
            np[k].sort()

            for t, y, v in np[k]:
                if t == 0:
                    ft.update(y, v)
                else:
                    res[v] = ft.query(y)

        return res


"""
x = [4, 3, 1, 2]
y = [2, 4, 9, 5]
x = [4, 3, 2, 1]
y = [2, 4, 5, 9]
queries=[[4, 1], [1, 3], [2, 5]]
queries=[[4, 1], [2, 5], [1, 3]]

"""

s = Solution()
print(s.maximumSumQueries(nums1=[4, 3, 1, 2], nums2=[2, 4, 9, 5], queries=[[4, 1], [1, 3], [2, 5]]))
print(s.maximumSumQueries(nums1=[3, 2, 5], nums2=[2, 3, 4], queries=[[4, 4], [3, 2], [1, 1]]))
print(s.maximumSumQueries(nums1=[2, 1], nums2=[2, 3], queries=[[3, 3]]))
