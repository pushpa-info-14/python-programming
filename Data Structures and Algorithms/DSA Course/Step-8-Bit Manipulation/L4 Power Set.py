def all_subsets(nums):
    n = len(nums)
    sets = []

    for num in range(1 << n):
        cur = []
        i = 0
        while num:
            if num & 1:
                cur.append(nums[i])
            i += 1
            num = num >> 1
        sets.append(cur)

    return sets


def all_subsets2(nums):
    n = len(nums)
    sets = []

    for num in range(1 << n):
        cur = []
        for i in range(n):
            if num & 1 << i:
                cur.append(nums[i])
        sets.append(cur)

    return sets


print(all_subsets([1, 2, 3]))
print(all_subsets2([1, 2, 3]))
