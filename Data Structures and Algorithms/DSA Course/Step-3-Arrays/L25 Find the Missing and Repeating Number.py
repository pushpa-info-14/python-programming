def findMissingBetter(nums):
    n = len(nums)
    mp = [0] * (n + 1)
    for i in range(n):
        mp[nums[i]] += 1
    repeating = -1
    missing = -1
    for i in range(1, n + 1):
        if mp[i] == 0:
            missing = i
        elif mp[i] == 2:
            repeating = i

        if missing != -1 and repeating != -1:
            break
    return [repeating, missing]


def findMissingOptimal1(nums):
    n = len(nums)
    # x = repeating
    # y = missing
    # s - sn =  x - y
    # s2 - s2n = x² - y² = (x - y)(x + y)
    sn = n * (n + 1) // 2
    s2n = n * (n + 1) * (2 * n + 1) // 6
    s = 0
    s2 = 0
    for i in range(n):
        s += nums[i]
        s2 += nums[i] * nums[i]

    val1 = s - sn  # x - y
    val2 = s2 - s2n  # x² - y²
    val2 = val2 // val1  # x + y
    x = (val1 + val2) // 2
    y = val2 - x

    return [x, y]


def findMissingOptimal2(nums):
    n = len(nums)
    xor = 0
    for i in range(n):
        xor ^= nums[i]
        xor ^= (i + 1)

    # number = xor & ~(xor - 1)

    bit = 0
    while xor > 0:
        if xor & 1 << bit:  # xor & number
            break
        bit += 1

    one = 0
    zero = 0
    for i in range(n):
        # part of 1 club
        if nums[i] & 1 << bit:  # xor & number
            one ^= nums[i]
        else:  # part of 0 club
            zero ^= nums[i]

    for i in range(1, n + 1):
        # part of 1 club
        if i & 1 << bit:
            one ^= i
        else:  # part of 0 club
            zero ^= i

    cnt = 0
    for i in range(n):
        if nums[i] == zero:
            cnt += 1

    if cnt == 2:
        repeating = zero
        missing = one
    else:
        repeating = one
        missing = zero

    return [repeating, missing]


print(findMissingBetter([4, 3, 6, 2, 1, 1]))
print(findMissingOptimal1([4, 3, 6, 2, 1, 1]))
print(findMissingOptimal2([4, 3, 6, 2, 1, 1]))
