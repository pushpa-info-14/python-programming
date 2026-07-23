from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                mul = nums[i] * nums[j]
                product_count[mul] += 1

        total_pairs = 0
        for key in product_count.keys():
            if product_count[key] > 1:
                pairs = product_count[key]
                total_pairs += 8 * pairs * (pairs - 1) // 2  # Combinations n!/r!(n-r)! n = pairs r = 2

        return total_pairs

    def tupleSameProduct2(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                count += 8 * product_count[product]
                product_count[product] += 1
        return count


s = Solution()
print(s.tupleSameProduct([2, 3, 4, 6]))
print(s.tupleSameProduct2([2, 3, 4, 6]))
