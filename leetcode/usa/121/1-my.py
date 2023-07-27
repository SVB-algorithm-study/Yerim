class Solution(object):
    def maxProfit(self, prices):
        # iterate prices 
        # 1. update min
        # 2. update ans
        ans = 0
        buy = prices[0]
        for p in prices:
            if p > buy:
                ans = max(ans, p - buy)
            else:
                buy = p
        return ans