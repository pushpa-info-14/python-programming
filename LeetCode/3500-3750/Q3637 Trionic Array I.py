from collections import defaultdict
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        counter = defaultdict(int)
        state = 0
        count = 0
        for i in range(1, n):
            if state == 0 and nums[i - 1] < nums[i]:
                count += 1
            elif state == 0 and nums[i - 1] >= nums[i]:
                counter[state] = count
                state = 1
                count = 1 if nums[i - 1] > nums[i] else 0
                continue
            elif state == 1 and nums[i - 1] > nums[i]:
                count += 1
            elif state == 1 and nums[i - 1] <= nums[i]:
                counter[state] = count
                state = 2
                count = 1 if nums[i - 1] < nums[i] else 0
                continue
            elif state == 2 and nums[i - 1] < nums[i]:
                count += 1
            elif state == 2 and nums[i - 1] >= nums[i]:
                counter[state] = count
                break
        counter[state] = count
        for x in range(3):
            if counter[x] == 0:
                return False
        return counter[0] + counter[1] + counter[2] == n - 1

    def isTrionic2(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        i = 1
        while i < n and nums[i - 1] < nums[i]:
            count += 1
            i += 1
        if count == 0:
            return False
        count = 0
        while i < n and nums[i - 1] > nums[i]:
            count += 1
            i += 1
        if count == 0:
            return False
        count = 0
        while i < n and nums[i - 1] < nums[i]:
            count += 1
            i += 1
        if count == 0 or i != n:
            return False
        return True


s = Solution()
print(s.isTrionic(nums=[1, 3, 5, 4, 2, 6]))
print(s.isTrionic(nums=[2, 1, 3]))
print(s.isTrionic(nums=[2, 4, 3, 3]))
print(s.isTrionic2(nums=[1, 3, 5, 4, 2, 6]))
print(s.isTrionic2(nums=[2, 1, 3]))
print(s.isTrionic2(nums=[2, 4, 3, 3]))
