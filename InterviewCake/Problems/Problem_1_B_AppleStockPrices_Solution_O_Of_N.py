#!/usr/bin/python

"""This program takes the list of stock prices and returns
   the best profit from 1 purchase and 1 sale of stock.
   It has nested loops and thus performance would be
   O(n)."""


def maximum_profit(stock_prices_yesterday):
    # using greedy approach calculate base max_profit
    # subtracting value at index 0 from value at index 1
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    # consider index value at 0 as min price
    min_price = stock_prices_yesterday[0]

    if len(stock_prices_yesterday) < 0:
        print("We need two values to check stock prices profit.")
    for i in range(len(stock_prices_yesterday)):
        # current price is stock price at index i
        current_price = stock_prices_yesterday[i]
        # calculate potential profit subtracting min
        # price from current price
        potential_profit = current_price - min_price
        # calculate max profit
        max_profit = max(max_profit, potential_profit)
        # calculate min price
        min_price = min(min_price, current_price)
    return max_profit, min_price

# stock = [10, 7, 5, 8, 11, 9, 26, 21, 45, 11, 3, 1000, 99, 45]
# print(maximum_profit(stock))