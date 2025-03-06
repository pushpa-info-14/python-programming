# i < j && a[i] > 2 x a[j]

def reversePairsBrute(nums):
    n = len(nums)
    res = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
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


def countPairs(arr, low, mid, high):
    cnt = 0
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt


def mergeSort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2
        cnt += mergeSort(arr, low, mid)
        cnt += mergeSort(arr, mid + 1, high)
        cnt += countPairs(arr, low, mid, high)
        merge(arr, low, mid, high)
    return cnt


def reversePairsOptimal(nums):
    res = mergeSort(nums, 0, len(nums) - 1)
    print(nums)
    return res


print(reversePairsBrute([40, 25, 19, 12, 9, 6, 2]))
print(reversePairsOptimal([40, 25, 19, 12, 9, 6, 2]))
