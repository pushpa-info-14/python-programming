from collections import defaultdict


def majorityElement(nums):
    n = len(nums)
    mp = defaultdict(int)

    for num in nums:
        mp[num] += 1

    for num in nums:
        if mp[num] > n / 2:
            return num
    return 0


def majorityElement2(nums):
    n = len(nums)
    element = 0
    count = 0

    for i in range(n):
        if count == 0:
            element = nums[i]
            count = 1
        elif element == nums[i]:
            count += 1
        else:
            count -= 1

    # Not required if a majority element always exists
    count = 0
    for num in nums:
        if num == element:
            count += 1

    if count > n / 2:
        return element
    return -1


print(majorityElement([2, 2, 3, 3, 1, 2, 2]))

# Moore's Voting Algorithm
print(majorityElement2([2, 2, 3, 3, 1, 2, 2]))
