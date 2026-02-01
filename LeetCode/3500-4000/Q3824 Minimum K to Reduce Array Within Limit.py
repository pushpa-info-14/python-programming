from typing import List


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def check(k):
            operations = 0
            for num in nums:
                operations += num // k
                if num % k:
                    operations += 1
            return operations <= k * k

        res = 0
        low, high = 1, 10 ** 5
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


s = Solution()
print(s.minimumK(nums=[3, 7, 5]))
print(s.minimumK(nums=[1]))
