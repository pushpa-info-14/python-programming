def longestIncreasingSubsequence(nums):
    n = len(nums)

    def dfs(index, prev_index):
        if index == n:
            return 0
        length = 0 + dfs(index + 1, prev_index)  # Not take
        if prev_index == -1 or nums[index] > nums[prev_index]:
            length = max(length, 1 + dfs(index + 1, index))
        return length

    return dfs(0, -1)


def longestIncreasingSubsequenceMemo(nums):
    n = len(nums)
    dp = [[-1] * (n + 1) for _ in range(n)]

    def dfs(index, prev_index):
        if index == n:
            return 0
        if dp[index][prev_index + 1] != -1:
            return dp[index][prev_index + 1]
        length = 0 + dfs(index + 1, prev_index)  # Not take
        if prev_index == -1 or nums[index] > nums[prev_index]:
            length = max(length, 1 + dfs(index + 1, index))

        dp[index][prev_index + 1] = length
        return length

    return dfs(0, -1)


print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequenceMemo([10, 9, 2, 5, 3, 7, 101, 18]))
