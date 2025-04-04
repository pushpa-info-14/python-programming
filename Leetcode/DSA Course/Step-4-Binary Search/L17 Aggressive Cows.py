from typing import List


def canPlace(stalls: List[int], cows, distance):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= distance:
            count += 1
            last = stalls[i]
    if count >= cows:
        return True
    else:
        return False


def minDistance(stalls: List[int], cows: int):
    stalls.sort()

    low, high = 1, stalls[-1] - stalls[0]  # max - min
    while low <= high:
        mid = (low + high) // 2
        if canPlace(stalls, cows, mid):
            low = mid + 1
        else:
            high = mid - 1
    return high


# Minimum distance between cows is maximum
print(minDistance([0, 3, 4, 7, 10, 9], 4))
