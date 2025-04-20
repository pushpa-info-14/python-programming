from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (abs(arr[i] - arr[j]) <= a and
                            abs(arr[j] - arr[k]) <= b and
                            abs(arr[i] - arr[k]) <= c):
                        res += 1

        return res

    def countGoodTriplets2(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        prefix_count = [0] * 1001
        res = 0
        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    # How many values before j
                    # where abs conditions are met
                    l = max(arr[j] - a, arr[k] - c)
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(l, 0)
                    r = min(r, 1000)
                    if l <= r:
                        res += prefix_count[r] - (0 if l == 0 else prefix_count[l - 1])
            for index in range(arr[j], 1001):
                prefix_count[index] += 1
        return res


s = Solution()
print(s.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
print(s.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
print(s.countGoodTriplets2(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
print(s.countGoodTriplets2(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
