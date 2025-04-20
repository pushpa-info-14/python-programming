def fourSumBrute(nums, target):
    n = len(nums)
    hashset = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if cur_sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        hashset.add(tuple(temp))

    return [list(i) for i in hashset]


def fourSumBetter(nums, target):
    n = len(nums)
    hashset = set()

    for i in range(n):
        for j in range(i + 1, n):
            seen = set()
            for k in range(j + 1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in seen:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    hashset.add(tuple(temp))
                seen.add(nums[k])

    return [list(i) for i in hashset]


def fourSumOptimal(nums, target):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]: continue
            k = j + 1
            l = n - 1
            while k < l:
                cur_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if cur_sum == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif cur_sum < target:
                    k += 1
                else:
                    l -= 1
    return res


print(fourSumBrute([1, 0, -1, 0, -2, 2], 0))
print(fourSumBrute([2, 2, 2, 2, 2], 8))
print(fourSumBetter([1, 0, -1, 0, -2, 2], 0))
print(fourSumBetter([2, 2, 2, 2, 2], 8))
print(fourSumOptimal([1, 0, -1, 0, -2, 2], 0))
print(fourSumOptimal([2, 2, 2, 2, 2], 8))
