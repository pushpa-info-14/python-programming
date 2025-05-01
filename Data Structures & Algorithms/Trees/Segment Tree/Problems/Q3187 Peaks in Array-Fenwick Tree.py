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


def isPeak(nums, index):
    if 0 <= index and index + 1 < len(nums) and nums[index - 1] < nums[index] > nums[index + 1]:
        return True
    return False


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ft = FenwickTree(n)

        for i in range(1, n - 1):
            if isPeak(nums, i):
                ft.update(i, 1)

        res = []
        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                if r - l < 2:  # At least 3 elements should exist to have a peak
                    res.append(0)
                else:
                    res.append((ft.query(r - 1) - ft.query(l)))
            else:
                index, val = query[1], query[2]
                prv = index - 1
                nxt = index + 1
                nums[index] = val

                for i in range(prv, nxt + 1):
                    if i > 0 and i + 1 < n:
                        peak_count = ft.query(i) - ft.query(i - 1)
                        if isPeak(nums, i):
                            ft.update(i, -peak_count + 1)
                        else:
                            ft.update(i, -peak_count)
        return res


s = Solution()
print(s.countOfPeaks(nums=[3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]]))
print(s.countOfPeaks(nums=[4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]]))
print(s.countOfPeaks(nums=[7, 10, 7], queries=[[1, 2, 2], [2, 0, 6], [1, 0, 2]]))
print(s.countOfPeaks(nums=[9, 7, 5, 8, 9], queries=[[2, 0, 2], [1, 0, 3], [1, 3, 3], [2, 3, 5]]))
