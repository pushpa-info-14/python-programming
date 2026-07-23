from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen = set()
        for start, end in nums:
            seen.update([x for x in range(start, end + 1)])
        return len(seen)

    def numberOfPoints2(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        prev_start, prev_end = nums[0]
        for start, end in nums[1:]:
            if prev_end < start:
                res += prev_end - prev_start + 1
                prev_start = start
            prev_start = min(prev_start, start)
            prev_end = max(prev_end, end)
        return res + prev_end - prev_start + 1


s = Solution()
print(s.numberOfPoints(nums=[[3, 6], [1, 5], [4, 7]]))
print(s.numberOfPoints(nums=[[1, 3], [5, 8]]))
print("---------")
print(s.numberOfPoints2(nums=[[3, 6], [1, 5], [4, 7]]))
print(s.numberOfPoints2(nums=[[1, 3], [5, 8]]))
