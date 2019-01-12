
#def get_max_profit(stock_prices):
#	max_profit = stock_prices[1] - stock_prices[0]
#	for a_idx, a_val in enumerate(stock_prices):
#		for b_idx, b_val in enumerate(stock_prices):
#			if a_idx < b_idx:
#				if b_val - a_val > max_profit:
#					max_profit = b_val - a_val
#	return max_profit

# def get_max_profit(stock_prices):
# 	min_price = stock_prices[0]
# 	max_profit = -6
# 	for current_price in stock_prices:
# 		min_price = min(min_price, current_price)
# 		current_profit = current_price - min_price
# 		max_profit = max(current_profit, max_profit)
# 	return max_profit

## problems with this is - does not consider if they are happening in diff times



## To fix - should be comparing 2 diff idx

#def get_max_profit(stock_prices):
#	min_price = stock_prices[0]
#	max_profit = stock_prices[1] - stock_prices[0]
#	for current_price in stock_prices:
#		
#		min_price = min(min_price, current_price)
#		current_profit = current_price - min_price
#		max_profit = max(current_profit, max_profit)
#	return max_profit


def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit





stock_prices = [5,4,4]


print(get_max_profit(stock_prices))
# Returns 6 (buying for $5 and selling for $11)
