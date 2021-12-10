# given a list of daily stock prices:
# find the maximum profit that could be made buying and selling the stock
# each index represents the price for that day
# need to find the biggest positive difference between days where the buy index is < sell index
# profit = prices[buy_index] - prices[sell_index]
# find the biggest difference between prices with the stipulation that the higher price comes after the lower price

# dumb way
def maxProfit(prices):
    # initialize the max_profit:
    max_profit = 0
    # loop through prices
    for (i, buy_price) in enumerate(prices):
        for sell_index in range(i + 1, len(prices)):
            if prices[sell_index] - buy_price > max_profit:
                max_profit = prices[sell_index] - buy_price
    return max_profit



print(maxProfit([6, 3, 1, 2, 5, 4])) #--> 4
print(maxProfit([8, 5, 3, 1])) #--> 0
print(maxProfit([3, 100, 1, 97])) #--> 97

# max_profit = sell_price - buy_price
def maxProfit_opt(prices):
    # intialize max_profit to 0 and min_price found to prices[0]
    max_profit = 0
    buy_price = prices[0]
    # loop through the prices list:
    for (i, sell_price) in enumerate(prices):
        # if the price we're on minus the intial buy_price is greater than the max_profit...
        if sell_price - buy_price > max_profit:
            # adjust max_profit
            max_profit = sell_price - buy_price
        # if the price of this index is less than buy_price...
        if sell_price < buy_price:
            # set buy_price to this index value
            buy_price = sell_price
    # return the max profit
    return max_profit


print(maxProfit_opt([6, 3, 1, 2, 5, 4])) #--> 4
print(maxProfit_opt([8, 5, 3, 1])) #--> 0
print(maxProfit_opt([3, 100, 1, 97])) #--> 97