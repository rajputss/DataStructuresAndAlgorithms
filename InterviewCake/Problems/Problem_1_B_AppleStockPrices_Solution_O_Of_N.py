#!/usr/bin/python


def maximum_profit(stock_prices_yesterday):
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    min_price = stock_prices_yesterday[0]

    if len(stock_prices_yesterday) < 0:
        print("We need two values to check stock prices profit.")
    for i in range(len(stock_prices_yesterday)):
        current_price = stock_prices_yesterday[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit, min_price

# stock = [10, 7, 5, 8, 11, 9, 26, 21, 45, 11, 3, 1000, 99, 45]
# print(maximum_profit(stock))