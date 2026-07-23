from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + arr[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                if (j - i + 1) & 1:
                    res += pre_sum[j + 1] - pre_sum[i]
        return res

    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            left = i
            right = n - i - 1
            res += arr[i] * (left // 2 + 1) * (right // 2 + 1)
            res += arr[i] * ((left + 1) // 2) * ((right + 1) // 2)
        return res


s = Solution()
print(s.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays(arr=[1, 2]))
print(s.sumOddLengthSubarrays(arr=[10, 11, 12]))
print(s.sumOddLengthSubarrays2(arr=[1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays2(arr=[1, 2]))
print(s.sumOddLengthSubarrays2(arr=[10, 11, 12]))
