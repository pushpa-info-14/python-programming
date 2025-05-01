from typing import List


def fractionalKnapsack(items: List[List[int]], w: int):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    for value, weight in items:
        if weight < w:
            total_value += value
            w -= weight
        else:
            total_value += (value / weight) * w
            break

    return total_value


print(fractionalKnapsack([[100, 20], [60, 10], [100, 50], [200, 50]], 90))
