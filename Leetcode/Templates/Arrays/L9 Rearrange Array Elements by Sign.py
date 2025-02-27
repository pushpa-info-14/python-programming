def rearrange(nums):
    positives = []
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    for i in range(len(nums) // 2):
        nums[2 * i] = positives[i]
        nums[2 * i + 1] = negatives[i]
    return nums


def rearrange2(nums):
    n = len(nums)
    res = [0] * n
    p_index = 0
    n_index = 1
    for num in nums:
        if num < 0:
            res[n_index] = num
            n_index += 2
        else:
            res[p_index] = num
            p_index += 2

    return res


def rearrangeVariety2(nums):
    positives = []
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    p_len = len(positives)
    n_len = len(negatives)
    min_len = min(p_len, n_len)
    i = 0
    j = 0
    while i < min_len:
        nums[j] = positives[i]
        nums[j + 1] = negatives[i]
        i += 1
        j += 2
    while i < p_len:
        nums[j] = positives[i]
        i += 1
        j += 1
    while i < n_len:
        nums[j] = negatives[i]
        i += 1
        j += 1
    return nums


print(rearrange([3, 1, -2, -5, 2, -4]))
print(rearrange2([3, 1, -2, -5, 2, -4]))

print(rearrangeVariety2([-1, 2, 3, 4, -3, 1]))
