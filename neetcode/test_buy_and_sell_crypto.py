class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first, the definition of profit
        # profit = sell price - purchase price
        # constraints:
        # i = purchase index
        # j = sell index
        # j must be > i
        # only one purchase and only one sell

        # APPROACH 1
        # iterate through all possible options for i and j
        # track max_profit by comparing cur_profit to max_profit
        # TIME: O(n**2)
        # SPACE: O(n)

        # APPROACH 2
        # How can we make this linear or log linear (sort)?
        # i.e. iterate once, track key info
        # use stored info to determine max result

        len_prices = len(prices)
        max_profit = 0
        i = 0
        j = 1

        while j < len_prices:
            purchase_price = prices[i]
            sell_price = prices[j]
            if purchase_price < sell_price:
                profit = sell_price - purchase_price
                if profit > max_profit:
                    max_profit = profit
            else:
                i = i + 1
            j = j + 1

        # for i in range(len_prices):
        #     for j in range(len_prices):
        #         if j > i:
        #             purchase_price = prices[i]
        #             sell_price = prices[j]
        #             profit = sell_price - purchase_price
        #             if profit > max_profit:
        #                 max_profit = profit
        return max_profit
