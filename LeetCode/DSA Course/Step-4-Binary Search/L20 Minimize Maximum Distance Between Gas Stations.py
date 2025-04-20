import heapq
from typing import List


def minimizeMaxDistance(nums: List[int], k: int):
    n = len(nums)
    how_many = [0] * (n - 1)

    for g in range(k):
        max_val = -1
        max_index = -1
        for i in range(n - 1):
            diff = nums[i + 1] - nums[i]
            section_length = diff / (how_many[i] + 1)
            if max_val < section_length:
                max_val = section_length
                max_index = i
        how_many[max_index] += 1

    res = -1
    for i in range(n - 1):
        diff = nums[i + 1] - nums[i]
        section_length = diff / (how_many[i] + 1)
        res = max(res, section_length)
    return res


def minimizeMaxDistance2(nums: List[int], k: int):
    n = len(nums)
    how_many = [0] * (n - 1)
    max_heap = []

    for i in range(n - 1):
        diff = nums[i + 1] - nums[i]
        heapq.heappush(max_heap, (-diff, i))

    for g in range(k):
        top = heapq.heappop(max_heap)
        section_index = top[1]
        how_many[section_index] += 1

        diff = nums[section_index + 1] - nums[section_index]
        section_length = diff / (how_many[section_index] + 1)
        heapq.heappush(max_heap, (-section_length, section_index))

    return -heapq.heappop(max_heap)[0]


def numOfGasStationsRequired(nums, distance: float):
    count = 0
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        number_in_between = int(diff / distance)
        if diff == number_in_between * distance:
            number_in_between -= 1
        count += number_in_between
    return count


def minimizeMaxDistance3(nums: List[int], k: int):
    n = len(nums)
    low = 0.0
    high = 0.0
    for i in range(n - 1):
        high = max(high, nums[i + 1] - nums[i])

    while high - low > 1e-6:
        mid = (low + high) / 2.0
        count = numOfGasStationsRequired(nums, mid)
        if count > k:
            low = mid
        else:
            high = mid
    return high  # polarity will not work here


# Bruteforce
print(minimizeMaxDistance([1, 2, 3, 4, 5], 4))
print(minimizeMaxDistance([1, 13, 17, 23], 5))

# Heap
print(minimizeMaxDistance2([1, 2, 3, 4, 5], 4))
print(minimizeMaxDistance2([1, 13, 17, 23], 5))

# Binary Search
print(minimizeMaxDistance3([1, 2, 3, 4, 5], 4))
print(minimizeMaxDistance3([1, 13, 17, 23], 5))
