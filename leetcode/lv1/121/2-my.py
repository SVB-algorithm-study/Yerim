class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        m = prices[0]
        for p in prices:
            m = min(m, p)
            ans = max(ans, p-m)
        return ans