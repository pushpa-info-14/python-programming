def max_sum(nums):
    n = len(nums)
    prev = nums[0]
    prev2 = 0

    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += prev2
        not_pick = prev
        cur = max(pick, not_pick)
        prev2 = prev
        prev = cur

    return prev


def house_robber2(houses):
    if len(houses) == 1: return houses[0]
    array1 = houses[1:]
    array2 = houses[:-1]

    return max(max_sum(array1), max_sum(array2))


print(house_robber2([2, 3, 2]))
print(house_robber2([1, 2, 3, 1]))
