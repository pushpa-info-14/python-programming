from typing import List


def missingNumber(nums: List[int]) -> int:
    total = 0
    expectedTotal = 0
    for i in range(len(nums)):
        total += nums[i]
        expectedTotal += i + 1

    return expectedTotal - total


print(missingNumber([9,6,4,2,3,5,7,0,1]))
