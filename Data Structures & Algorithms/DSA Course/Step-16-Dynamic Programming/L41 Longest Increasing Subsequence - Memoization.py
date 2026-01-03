def longestIncreasingSubsequence(nums):
    n = len(nums)

    def dfs(index, prev_index):
        if index == n:
            return 0
        cur = 0 + dfs(index + 1, prev_index)  # Not take
        if prev_index == -1 or nums[index] > nums[prev_index]:
            cur = max(cur, 1 + dfs(index + 1, index))
        return cur

    return dfs(0, -1)


def longestIncreasingSubsequence2(nums):
    n = len(nums)
    dp = [[-1] * (n + 1) for _ in range(n)]

    def dfs(index, prev_index):
        if index == n:
            return 0
        if dp[index][prev_index + 1] != -1:
            return dp[index][prev_index + 1]
        cur = 0 + dfs(index + 1, prev_index)  # Not take
        if prev_index == -1 or nums[index] > nums[prev_index]:
            cur = max(cur, 1 + dfs(index + 1, index))

        dp[index][prev_index + 1] = cur
        return cur

    return dfs(0, -1)


print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequence2([10, 9, 2, 5, 3, 7, 101, 18]))
