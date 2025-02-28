def maxProfit(stocks):
    max_profit = 0
    min_stock = stocks[0]

    for i in range(1, len(stocks)):
        profit = stocks[i] - min_stock
        max_profit = max(max_profit, profit)
        min_stock = min(min_stock, stocks[i])
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
