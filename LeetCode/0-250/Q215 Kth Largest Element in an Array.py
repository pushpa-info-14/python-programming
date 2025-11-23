import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for num in nums:
            heapq.heappush(q, -num)
        res = 0
        for i in range(k):
            res = -(heapq.heappop(q))
        return res

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(s.findKthLargest2([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
