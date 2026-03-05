from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]

        inf = 10 ** 20
        count_odd = 0  # The number of operations we need if the first element is odd
        count_even = 0  # The number of operations we need if the first element is even
        for i in range(n):
            if i % 2 != nums[i] % 2:  # even first
                count_even += 1
            else:
                count_odd += 1

        mn = min(nums)
        mx = max(nums)
        best = inf
        if count_even <= count_odd:
            keep_min = keep_max = False
            for i in range(n):
                if i % 2 == nums[i] % 2:  # We cannot change this for even
                    if nums[i] == mn:
                        keep_min = True
                    elif nums[i] == mx:
                        keep_max = True
            new_min = mn
            if not keep_min:
                new_min += 1
            new_max = mx
            if not keep_max:
                new_max -= 1
            best = min(best, max(new_max - new_min, 1))

        if count_odd <= count_even:
            keep_min = keep_max = False
            for i in range(n):
                if i % 2 != nums[i] % 2:  # We cannot change this for odd
                    if nums[i] == mn:
                        keep_min = True
                    elif nums[i] == mx:
                        keep_max = True
            new_min = mn
            if not keep_min:
                new_min += 1
            new_max = mx
            if not keep_max:
                new_max -= 1
            best = min(best, max(new_max - new_min, 1))

        return [min(count_odd, count_even), best]


s = Solution()
print(s.makeParityAlternating(nums=[-2, -3, 1, 4]))
print(s.makeParityAlternating(nums=[0, 2, -2]))
print(s.makeParityAlternating(nums=[7]))
