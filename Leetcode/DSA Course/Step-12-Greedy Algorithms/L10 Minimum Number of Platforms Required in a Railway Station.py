from typing import List


def calculateMinPlatforms(at: List[int], dt: List[int]):
    n = len(at)
    at.sort()
    dt.sort()

    res = 0
    cnt = 0
    i, j = 0, 0
    while i < n:
        if at[i] <= dt[j]:
            cnt += 1
            res = max(res, cnt)
            i += 1
        else:
            cnt -= 1
            j += 1
    return res


print(calculateMinPlatforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
print(calculateMinPlatforms([100, 200, 300, 400], [200, 300, 400, 500]))
