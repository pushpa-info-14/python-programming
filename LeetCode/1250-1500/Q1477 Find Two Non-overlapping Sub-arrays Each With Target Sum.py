class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        inf = 10 ** 10
        n = len(arr)
        prefix = [inf] * n
        suffix = [inf] * n
        l = 0
        total = 0
        cur = inf
        for r in range(n):
            while total > target and l <= r:
                total -= arr[l]
                l += 1
            if total == target:
                cur = min(cur, r - l)
            prefix[r] = cur
            total += arr[r]
        r = n - 1
        total = 0
        cur = inf
        for l in range(n - 1, -1, -1):
            total += arr[l]
            while total > target and l <= r:
                total -= arr[r]
                r -= 1
            if total == target:
                cur = min(cur, r - l + 1)
            suffix[l] = cur
        res = inf
        for i in range(n):
            if prefix[i] == inf or suffix[i] == inf:
                continue
            res = min(res, prefix[i] + suffix[i])
        return res if res != inf else -1


s = Solution()
print(s.minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))
print(s.minSumOfLengths(arr=[7, 3, 4, 7], target=7))
print(s.minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))
print(s.minSumOfLengths(arr=[1, 6, 1], target=7))
print(s.minSumOfLengths(arr=[1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], target=5))
print(
    s.minSumOfLengths(arr=[2, 2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=20))
