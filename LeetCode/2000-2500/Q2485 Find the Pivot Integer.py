import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + i

        for i in range(1, n + 1):
            sum1 = pre_sum[i]
            sum2 = pre_sum[n] - pre_sum[i - 1]
            if sum1 == sum2:
                return i
        return -1

    def pivotInteger2(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = int(math.sqrt(total))
        return x if x * x == total else -1


s = Solution()
print(s.pivotInteger(8))
print(s.pivotInteger(1))
print(s.pivotInteger(4))
print(s.pivotInteger2(8))
print(s.pivotInteger2(1))
print(s.pivotInteger2(4))
