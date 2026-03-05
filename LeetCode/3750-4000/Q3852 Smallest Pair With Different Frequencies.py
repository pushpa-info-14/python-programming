from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        unique_nums = sorted(set(nums))
        x = unique_nums[0]
        for y in unique_nums[1:]:
            if counter[x] != counter[y]:
                return [x, y]
        return [-1, -1]


s = Solution()
print(s.minDistinctFreqPair(nums=[1, 1, 2, 2, 3, 4]))
print(s.minDistinctFreqPair(nums=[1, 5]))
print(s.minDistinctFreqPair(nums=[7]))
