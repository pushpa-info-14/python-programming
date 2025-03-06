# i < j & a[i] > a[j]

def countInversionsBrute(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                res += 1
    return res


def merge(arr, low, mid, high):
    temp = []
    cnt = 0
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            cnt += (mid - i + 1)
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return cnt


def mergeSort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2
        cnt += mergeSort(arr, low, mid)
        cnt += mergeSort(arr, mid + 1, high)
        cnt += merge(arr, low, mid, high)
    return cnt


def countInversionsOptimal(nums):
    res = mergeSort(nums, 0, len(nums) - 1)
    print(nums)
    return res


numsArray = [5, 4, 3, 2, 1]
mergeSort(numsArray, 0, len(numsArray) - 1)
print(numsArray)

print(countInversionsBrute([5, 3, 2, 4, 1]))
print(countInversionsOptimal([5, 3, 2, 4, 1]))
