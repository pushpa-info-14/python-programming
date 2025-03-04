from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        mp = [0] * n
        cur_max = 0
        last_index = 0

        for i in range(n):
            mp[i] = i
            for prev in range(i):
                if nums[i] % nums[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    mp[i] = prev
            if dp[i] > cur_max:
                cur_max = dp[i]
                last_index = i

        temp = [nums[last_index]]
        while mp[last_index] != last_index:
            last_index = mp[last_index]
            temp.append(nums[last_index])
        return temp[::-1]


s = Solution()
print(s.largestDivisibleSubset([1, 16, 7, 8, 4]))
