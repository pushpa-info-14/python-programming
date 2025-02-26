def missingNumber1(nums):
    n = len(nums)
    seen = set()

    for num in nums:
        seen.add(num)

    for i in range(1, n + 2):
        if i not in seen:
            return i


def missingNumber2(nums):
    n = len(nums)
    expected_sum = (n + 1) * (n + 2) // 2
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
    return expected_sum - cur_sum


def missingNumber3(nums):
    n = len(nums)
    xor = 0
    for i in range(1, n + 2):
        xor ^= i

    for i in range(n):
        xor ^= nums[i]
    return xor


def missingNumber4(nums):
    n = len(nums)
    xor = 0
    for i in range(n):
        xor ^= nums[i]
        xor ^= (i + 1)
    return xor ^ (n + 1)


def missingNumber5(nums):
    n = len(nums)

    for i in range(n):
        num = abs(nums[i])
        if num - 1 < n:
            nums[num - 1] = -nums[num - 1]

    for i in range(n):
        if nums[i] > 0:
            return i + 1


print(missingNumber1([2, 3, 4, 5]))
print(missingNumber1([2, 3, 1, 5]))
print(missingNumber2([2, 3, 4, 5]))
print(missingNumber2([2, 3, 1, 5]))
print(missingNumber3([2, 3, 4, 5]))
print(missingNumber3([2, 3, 1, 5]))
print(missingNumber4([2, 3, 4, 5]))
print(missingNumber4([2, 3, 1, 5]))
print(missingNumber5([2, 3, 4, 5]))
print(missingNumber5([2, 3, 1, 5]))
