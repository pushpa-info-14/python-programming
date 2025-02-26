def sortArray(nums):
    counts = [0, 0, 0]

    for num in nums:
        counts[num] += 1
    start = 0
    for i in range(counts[0]):
        nums[start] = 0
        start += 1
    for i in range(counts[1]):
        nums[start] = 1
        start += 1
    for i in range(counts[2]):
        nums[start] = 2
        start += 1
    return nums


def sortArray2(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(sortArray([0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]))

# Dutch National Flag Algorithm
# low, mid, high
# [0.........low - 1]
# [low.......mid - 1]
# [high + 1....n - 1]
print(sortArray2([0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
