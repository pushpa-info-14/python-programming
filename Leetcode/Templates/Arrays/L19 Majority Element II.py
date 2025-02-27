from collections import defaultdict


def majorityElement(nums):
    n = len(nums)
    mp = defaultdict(int)
    minimum = (n // 3) + 1
    res = []

    for num in nums:
        mp[num] += 1

        if mp[num] == minimum:
            res.append(num)
        if len(res) == 2:
            break
    return res


def majorityElement2(nums):
    n = len(nums)
    cnt1, cnt2 = 0, 0
    element1, element2 = 0, 0
    res = []
    minimum = n // 3

    for i in range(n):
        if cnt1 == 0 and nums[i] != element2:
            cnt1 = 1
            element1 = nums[i]
        elif cnt2 == 0 and nums[i] != element1:
            cnt2 = 1
            element2 = nums[i]
        elif nums[i] == element1:
            cnt1 += 1
        elif nums[i] == element2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    cnt1, cnt2 = 0, 0
    for num in nums:
        if element1 == num: cnt1 += 1
        if element2 == num: cnt2 += 1

    if cnt1 > minimum: res.append(element1)
    if cnt2 > minimum: res.append(element2)
    return res


print(majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
print(majorityElement2([1, 1, 1, 3, 3, 2, 2, 2]))
