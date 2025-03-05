def xorBrute(nums, k):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i, n):
            xor = 0
            for k in range(i, j + 1):
                xor = xor ^ nums[k]
            if xor == k:
                res += 1
    return res


def xorBetter(nums, k):
    n = len(nums)
    res = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor ^ nums[j]
            if xor == k:
                res += 1
    return res


def xorOptimal(nums, k):
    n = len(nums)
    seen = {0: 1}
    res = 0
    xor = 0
    for i in range(n):
        xor = xor ^ nums[i]
        rem = xor ^ k
        if rem in seen:
            res += seen[rem]
        if xor not in seen:
            seen[xor] = 0
        seen[xor] += 1

    return res


print(xorBrute([4, 2, 2, 6, 4], 6))
print(xorBetter([4, 2, 2, 6, 4], 6))
print(xorOptimal([4, 2, 2, 6, 4], 6))
