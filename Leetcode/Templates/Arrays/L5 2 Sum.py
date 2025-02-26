def canSum(nums, target):
    n = len(nums)
    mp = {}

    for i in range(n):
        if nums[i] in mp:
            return True
        mp[target - nums[i]] = i

    return False

def canSum2(nums, target):
    n = len(nums)
    nums.sort()

    l,r=0,n-1
    while l < r:
        cur_sum = nums[l] + nums[r]
        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            return True
    return False


def twoSum(nums, target):
    n = len(nums)
    mp = {}

    for i in range(n):
        if nums[i] in mp:
            return [mp[nums[i]], i]
        mp[target - nums[i]] = i

    return [-1, -1]


print(canSum([2, 6, 5, 8, 11], 14))
print(canSum2([2, 6, 5, 8, 11], 14))

print(twoSum([2, 6, 5, 8, 11], 14))
