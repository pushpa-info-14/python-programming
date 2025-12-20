from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        memo = {}  # (i, prev) -> []

        def dfs(i, prev):
            if i == n:
                return []
            if (i, prev) in memo:
                return memo[(i, prev)]

            res = dfs(i + 1, prev)  # skip nums[i]
            if nums[i] % prev == 0:
                temp = [nums[i]] + dfs(i + 1, nums[i])  # include nums[i]
                res = temp if len(temp) > len(res) else res
            memo[(i, prev)] = res
            return res

        return dfs(0, 1)

    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        memo = {}  # i -> []

        def dfs(i):
            if i == n:
                return []
            if i in memo: return memo[i]

            res = [nums[i]]
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp
            memo[i] = res
            return res

        ans = []
        for index in range(n):
            temp_ans = dfs(index)  # skip nums[i]
            if len(temp_ans) > len(ans):
                ans = temp_ans

        return ans

    def largestDivisibleSubset3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[num] for num in nums]
        res = []
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    if len(temp) > len(dp[i]):
                        dp[i] = temp
            if len(dp[i]) > len(res):
                res = dp[i]
        return res

    def largestDivisibleSubset4(self, nums: List[int]) -> List[int]:
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


# LeetCode 368
s = Solution()
print(s.largestDivisibleSubset([1, 16, 7, 8, 4]))
print(s.largestDivisibleSubset([1, 2, 3]))
print(s.largestDivisibleSubset([1, 2, 4, 8]))
print("-----------------------------------------")
print(s.largestDivisibleSubset2([1, 16, 7, 8, 4]))
print(s.largestDivisibleSubset2([1, 2, 3]))
print(s.largestDivisibleSubset2([1, 2, 4, 8]))
print("-----------------------------------------")
print(s.largestDivisibleSubset3([1, 16, 7, 8, 4]))
print(s.largestDivisibleSubset3([1, 2, 3]))
print(s.largestDivisibleSubset3([1, 2, 4, 8]))
print("-----------------------------------------")
print(s.largestDivisibleSubset4([1, 16, 7, 8, 4]))
print(s.largestDivisibleSubset4([1, 2, 3]))
print(s.largestDivisibleSubset4([1, 2, 4, 8]))
