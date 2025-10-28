from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        original = nums.copy()
        n = len(nums)
        initial_zeros = original.count(0)
        increment = {-1: -1, 1: 1}
        res = 0
        for i in range(n):
            if original[i] != 0:
                continue
            for d in [-1, 1]:  # -1 - left, 1 - right
                zeros = initial_zeros
                curr = i
                curr += increment[d]
                nums = original.copy()
                while 0 <= curr < n:
                    if nums[curr] == 0:
                        curr += increment[d]
                    elif nums[curr] > 0:
                        nums[curr] -= 1
                        if nums[curr] == 0:
                            zeros += 1
                        d = -d
                        curr += increment[d]
                if zeros == n:
                    res += 1
        return res

    def countValidSelections2(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum_l = [0] * n
        prefix_sum_r = [0] * n
        cur = 0
        for i in range(n):
            prefix_sum_l[i] = cur
            cur += nums[i]
        cur = 0
        for i in range(n - 1, -1, -1):
            prefix_sum_r[i] = cur
            cur += nums[i]

        res = 0
        for i in range(n):
            if nums[i] == 0:
                if prefix_sum_l[i] == prefix_sum_r[i]:
                    res += 2
                elif abs(prefix_sum_l[i] - prefix_sum_r[i]) == 1:
                    res += 1
        return res


s = Solution()
print(s.countValidSelections(nums=[1, 0, 2, 0, 3]))
print(s.countValidSelections(nums=[2, 3, 4, 0, 4, 1, 0]))
print(s.countValidSelections2(nums=[1, 0, 2, 0, 3]))
print(s.countValidSelections2(nums=[2, 3, 4, 0, 4, 1, 0]))
