# Printing all subsequences whose sum is k

def countSubEqualK(arr, k):
    n = len(arr)
    res = []

    def dfs(i, sub, summation):
        if i == n:
            if summation == k:
                res.append(sub.copy())
            return
        sub.append(arr[i])
        dfs(i + 1, sub, summation + arr[i])
        sub.pop()
        dfs(i + 1, sub, summation)

    dfs(0, [], 0)
    return res


print(countSubEqualK([1, 2, 1], 2))


# Print any subsequence whose sum is k

def anySubEqualK(arr, k):
    n = len(arr)
    res = [[]]

    def dfs(i, sub, summation):
        if i == n:
            if summation == k:
                res[0] = sub.copy()
                return True
            return False

        sub.append(arr[i])
        if dfs(i + 1, sub, summation + arr[i]):
            return True
        sub.pop()
        if dfs(i + 1, sub, summation):
            return True
        return False

    dfs(0, [], 0)
    return res[0]


print(anySubEqualK([1, 2, 1], 2))


# Count all subsequences whose sum is k

def countSubEqualK(arr, k):
    n = len(arr)

    def dfs(i, summation):
        if i == n:
            if summation == k:
                return 1
            return 0

        cnt = 0
        cnt += dfs(i + 1, summation + arr[i])
        cnt += dfs(i + 1, summation)
        return cnt

    return dfs(0, 0)


print(countSubEqualK([1, 2, 1], 2))
