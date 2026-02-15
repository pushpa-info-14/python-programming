from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        groups = []
        i = 0
        while i < n:
            cur = [nums[i]]
            i += 1
            while i < n and colors[i - 1] == colors[i]:
                cur.append(nums[i])
                i += 1
            groups.append(cur.copy())

        res = 0
        for group in groups:
            odd = 0
            even = 0
            for i in range(len(group)):
                if i & 1:
                    odd += group[i]
                else:
                    even += group[i]
            res += max(odd, even)
        return res


s = Solution()
print(s.rob(nums=[1, 4, 3, 5], colors=[1, 1, 2, 2]))
print(s.rob(nums=[3, 1, 2, 4], colors=[2, 3, 2, 2]))
print(s.rob(nums=[10, 1, 3, 9], colors=[1, 1, 1, 2]))
