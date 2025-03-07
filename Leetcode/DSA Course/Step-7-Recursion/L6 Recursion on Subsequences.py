# Print all subsequences

def subsequences(arr):
    n = len(arr)
    res = []

    def dfs(i, sub):
        if i == n:
            res.append(sub.copy())
            return
        sub.append(arr[i])
        dfs(i + 1, sub)  # Take
        sub.pop()
        dfs(i + 1, sub)  # Not take

    dfs(0, [])
    return res


print(subsequences([3, 1, 2]))
