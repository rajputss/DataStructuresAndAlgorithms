#!/usr/bin/python


def maximum_profit(stock_prices_yesterday):
    max_profit = 0
    for i in range(len(stock_prices_yesterday)):
        for j in range(len(stock_prices_yesterday)):
            earlier_time = min(i, j)
            later_time = max(i, j)
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price = stock_prices_yesterday[later_time]
            potential_profit = later_price - earlier_price
            max_profit = max(potential_profit, max_profit)
    return max_profit

# stock = [10, 7, 5, 8, 11, 9]
stock = [10, 7, 5, 8, 11, 9, 26, 21, 45, 11, 3, 1000, 99, 45]
print(maximum_profit(stock))