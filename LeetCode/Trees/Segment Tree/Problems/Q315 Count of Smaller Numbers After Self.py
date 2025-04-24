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
            res[index] = ft.query(n - 1) - ft.query(index - 1)  # Range [index, n - 1]
            ft.update(index, 1)
        return res

    def countSmaller2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        def merge(pairs, low, mid, high):
            temp = [0] * (high - low + 1)
            i = low
            j = mid + 1
            k = 0
            while i <= mid and j <= high:
                if pairs[i][0] > pairs[j][0]:
                    res[pairs[i][1]] += high - j + 1
                    temp[k] = pairs[i]
                    k += 1
                    i += 1
                else:
                    temp[k] = pairs[j]
                    k += 1
                    j += 1
            while i <= mid:
                temp[k] = pairs[i]
                k += 1
                i += 1
            while j <= high:
                temp[k] = pairs[j]
                k += 1
                j += 1

            for i in range(low, high + 1):
                pairs[i] = temp[i - low]

        def mergeSort(pairs, low, high):
            if low < high:
                mid = low + (high - low) // 2
                mergeSort(pairs, low, mid)
                mergeSort(pairs, mid + 1, high)
                merge(pairs, low, mid, high)

        num_pairs = [(num, i) for i, num in enumerate(nums)]
        mergeSort(num_pairs, 0, n - 1)
        return res


s = Solution()
print(s.countSmaller([5, 2, 6, 1]))
print(s.countSmaller([-1]))
print(s.countSmaller([-1, -1]))

print(s.countSmaller2([5, 2, 6, 1]))
print(s.countSmaller2([-1]))
print(s.countSmaller2([-1, -1]))
print(s.countSmaller2([1, 9, 7, 8, 5]))
