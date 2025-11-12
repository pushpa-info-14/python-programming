from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        n = len(nums)
        one_count = 0
        cur_gcd = 0
        for num in nums:
            cur_gcd = gcd(cur_gcd, num)
            if num == 1:
                one_count += 1
        if one_count > 0:
            return n - one_count
        if cur_gcd != 1:
            return -1

        min_sub_len = 10 ** 10
        for l in range(n):
            cur_gcd = 0
            for r in range(l, n):
                if r - l + 1 >= min_sub_len:
                    break
                cur_gcd = gcd(cur_gcd, nums[r])
                if cur_gcd == 1:
                    min_sub_len = r - l + 1
                    break
        return min_sub_len - 1 + n - 1


s = Solution()
print(s.minOperations(nums=[2, 6, 3, 4]))
print(s.minOperations(nums=[2, 10, 6, 14]))
