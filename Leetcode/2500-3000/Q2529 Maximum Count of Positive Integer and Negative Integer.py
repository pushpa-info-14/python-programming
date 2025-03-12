from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1

        return max(neg, pos)

    def maximumCount2(self, nums: List[int]) -> int:
        n = len(nums)
        def find_left(target):
            l,r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        first_non_negative = find_left(0)
        first_positive = find_left(1)
        neg = first_non_negative
        pos = n - first_positive

        return max(neg, pos)


s = Solution()
print(s.maximumCount([-2, -1, -1, 1, 2, 3]))
print(s.maximumCount([-3, -2, -1, 0, 0, 1, 2]))
print(s.maximumCount([5, 20, 66, 1314]))
print(s.maximumCount2([-2, -1, -1, 1, 2, 3]))
print(s.maximumCount2([-3, -2, -1, 0, 0, 1, 2]))
print(s.maximumCount2([5, 20, 66, 1314]))
