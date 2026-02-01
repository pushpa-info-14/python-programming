def lowerBound(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    target_index = -1
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
            target_index = mid
        else:
            return mid

    return target_index


def longestIncreasingSubsequence(nums):
    n = len(nums)
    temp = [nums[0]]
    res = 1

    for i in range(1, n):
        if nums[i] > temp[-1]:
            temp.append(nums[i])
            res += 1
        else:
            idx = lowerBound(temp, nums[i])
            temp[idx] = nums[i]
    # return len(temp)
    return res


print(lowerBound([1, 2, 3, 4, 7, 8], 2))
print(lowerBound([1, 2, 3, 4, 7, 8], 5))
print(lowerBound([1, 2, 3, 4, 7, 8], 8))
print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
