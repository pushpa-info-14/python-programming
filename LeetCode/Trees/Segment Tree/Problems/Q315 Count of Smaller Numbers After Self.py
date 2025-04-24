from typing import List


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def query(self, index):
        index += 1
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= (index & -index)
        return ans

    def update(self, index, val):
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += (index & -index)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        mapping = sorted([(num, i) for i, num in enumerate(nums)])
        ft = FenwickTree(n)
        for num, index in mapping:
            res[index] = ft.query(n - 1) - ft.query(index - 1) # Range [index, n - 1]
            ft.update(index, 1)
        return res


s = Solution()
print(s.countSmaller([5, 2, 6, 1]))
print(s.countSmaller([-1]))
print(s.countSmaller([-1, -1]))
