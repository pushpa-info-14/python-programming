"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction, design an algorithm to
find the maximum profit.

Note that you cannot sell stock before you buy one.

Example 1:

    Input: [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation:    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                    Note 7-1 = 6, as selling price needs to larger than buying price.
"""


def maximum_profit(prices):
    left, right = 0, 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit


print(maximum_profit([7, 1, 5, 3, 6, 4]))
