from typing import List


def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    maxVolume = 0

    while l < r:
        tempVolume = (r - l) * min(height[l], height[r])
        maxVolume = max(maxVolume, tempVolume)

        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1
    return maxVolume


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
