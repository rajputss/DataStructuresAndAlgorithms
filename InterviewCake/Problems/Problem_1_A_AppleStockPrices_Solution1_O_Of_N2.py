#!/usr/bin/python

"""This program takes the list of stock prices and returns
   the best profit from 1 purchase and 1 sale of stock.
   It has nested loops and thus performance would be
   O(n2)."""


def maximum_profit(stock_prices_yesterday):
    max_profit = 0
    for i in range(len(stock_prices_yesterday)):
        for j in range(len(stock_prices_yesterday)):
            # find the earliest and latest time between
            # index value i and j
            earlier_time = min(i, j)
            later_time = max(i, j)
            # find the earliest and latest price at index
            # earliest time and latest time respectively
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price = stock_prices_yesterday[later_time]
            # calculate potential profit
            potential_profit = later_price - earlier_price
            # get the maximum profit
            max_profit = max(potential_profit, max_profit)
    return max_profit

stock = [10, 7, 5, 8, 11, 9, 26, 21, 45, 11, 3, 1000, 99, 45]
print(maximum_profit(stock))