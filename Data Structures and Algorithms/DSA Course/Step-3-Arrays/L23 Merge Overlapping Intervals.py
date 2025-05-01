def mergeIntervalsBrute(arr):
    n = len(arr)
    arr.sort()
    res = []

    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        if len(res) > 0 and end <= res[-1][1]:
            continue
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        res.append([start, end])
    return res


def mergeIntervalsOptimal(arr):
    n = len(arr)
    arr.sort()
    res = []

    for i in range(n):
        if len(res) == 0 or arr[i][0] > res[-1][1]:
            res.append(arr[i])
        else:
            res[-1][1] = max(res[-1][1], arr[i][1])
    return res


print(mergeIntervalsBrute([[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]))
print(mergeIntervalsOptimal([[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]))
