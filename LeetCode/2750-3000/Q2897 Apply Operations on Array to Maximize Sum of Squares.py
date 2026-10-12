from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        bits = [0] * 30
        for num in nums:
            for i in range(30):
                bits[i] += (num >> i) & 1
        res = 0
        while k > 0:
            cur = 0
            for i in range(30):
                if bits[i] > 0:
                    cur = cur + (1 << i)
                    bits[i] -= 1
            res += cur ** 2
            res %= mod
            k -= 1
        return res


s = Solution()
print(s.maxSum(nums=[2, 6, 5, 8], k=2))
print(s.maxSum(nums=[4, 5, 4, 7], k=3))
