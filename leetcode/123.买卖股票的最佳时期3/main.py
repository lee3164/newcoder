# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
    """
    def maxProfit2(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """

        def helper(i, j):
            min_price = 2 ** 32 - 1
            max_profit = 0
            while i <= j:
                if prices[i] < min_price:
                    min_price = prices[i]
                elif prices[i] - min_price > max_profit:
                    max_profit = prices[i] - min_price
                i += 1
            return max_profit

        max_profit = 0
        i = 0
        while i < len(prices):
            profit = helper(0, i) + helper(i + 1, len(prices) - 1)
            if profit > max_profit:
                max_profit = profit
            i += 1

        return max_profit

    def maxProfit(self, prices):
        """
        两个dp数组，第一个表示前i天的最大收益，第二个表示第i天到最后一天的最大收益
        dp1从0开始，dp2从1开始
        """
        dp1 = {}
        dp2 = {}

        max_profit = 0
        min_price = prices[0]
        dp1[0] = 0
        dp1[1] = 0
        i = 1
        while i < len(prices):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            dp1[i + 1] = max_profit
            i += 1

        dp2[len(prices)] = 0
        max_price = prices[-1]
        max_profit = 0
        i = len(prices) - 2
        while i >= 0:
            if prices[i] > max_price:
                max_price = prices[i]
            elif max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
            dp2[i + 1] = max_profit
            i -= 1

        i = 0
        max_profit = 0
        while i < len(prices) - 1:
            if dp1[i] + dp2[i + 1] > max_profit:
                max_profit = dp1[i] + dp2[i + 1]
            i += 1

        return max_profit


if __name__ == '__main__':
    print Solution().maxProfit([7, 6, 4, 3, 1])
