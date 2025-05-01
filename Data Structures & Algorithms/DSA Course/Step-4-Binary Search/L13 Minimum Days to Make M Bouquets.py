from typing import List


def num_of_bouquets(bloom_days, day, k):
    count = 0
    bouquets_count = 0
    for bloom_day in bloom_days:
        if bloom_day <= day:
            count += 1
        else:
            bouquets_count += count // k
            count = 0
    bouquets_count += count // k
    return bouquets_count


def minimumDays(bloom_days: List[int], m: int, k: int):
    n = len(bloom_days)
    if n < m * k: return -1

    low, high = min(bloom_days), max(bloom_days)
    while low <= high:
        mid = (low + high) // 2
        possible_count = num_of_bouquets(bloom_days, mid, k)

        if possible_count < m:
            low = mid + 1
        else:
            high = mid - 1
    return low


# m = Number of bouquets
# k = Adjacent flowers required
print(minimumDays([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(minimumDays([1, 10, 3, 10, 2], 3, 2))
