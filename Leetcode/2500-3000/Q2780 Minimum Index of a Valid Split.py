from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dominant = 0
        count = 0
        for num in nums:
            if count == 0:
                dominant = num
            if num == dominant:
                count += 1
            else:
                count -= 1
        left_count = 0
        right_count = 0
        for num in nums:
            if num == dominant:
                right_count += 1

        for i in range(n):
            if nums[i] == dominant:
                left_count += 1
                right_count -= 1
            left_len = (i + 1)
            right_len = (n - i - 1)
            if 2 * left_count > left_len and 2 * right_count > right_len:
                return i
        return -1


s = Solution()
print(s.minimumIndex([1, 2, 2, 2]))
print(s.minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))
print(s.minimumIndex([3, 3, 3, 3, 7, 2, 2]))
