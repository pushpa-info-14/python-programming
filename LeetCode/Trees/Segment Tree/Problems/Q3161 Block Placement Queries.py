from typing import List


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def query(self, index):
        index += 1
        ans = 0
        while index > 0:
            ans = max(ans, self.tree[index])
            index -= (index & -index)
        return ans

    def update(self, index, val):
        index += 1
        while index < len(self.tree):
            self.tree[index] = max(self.tree[index], val)
            index += (index & -index)

def find(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def upperBound(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return low


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        blocks = []
        n = min(5 * 10000, 3 * len(queries)) + 1
        blocks.append(0)
        blocks.append(n)
        ft = FenwickTree(n)

        for query in queries:
            if query[0] == 1:
                blocks.append(query[1])
        blocks.sort()

        for i in range(1, len(blocks)):
            gap = blocks[i] - blocks[i - 1]
            x = blocks[i]
            ft.update(x, gap)

        ans = []
        for i in reversed(range(len(queries))):
            query = queries[i]
            if query[0] == 1:  # Remove the obstacle
                x = query[1]
                idx = find(blocks, x)
                prv = blocks[idx - 1]
                nxt = blocks[idx + 1]
                del blocks[idx]
                ft.update(nxt, nxt - prv)
            else:
                x, sz = query[1], query[2]
                upper_idx = upperBound(blocks, x)
                prv = blocks[upper_idx - 1]
                max_gap = max(ft.query(prv), x - prv)
                ans.append(max_gap >= sz)

        return ans[::-1]


# print(upperBound([1,2,2,4,4,5,6], 4))
# print(upperBound([1,2,2,4,4,5,6], 3))

s = Solution()
print(s.getResults(queries=[[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]))
print(s.getResults(queries=[[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]))
