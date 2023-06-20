class Solution(object):
    def maxProfit(self, prices):
        m = 0
        cmin = cmax = prices[0]
        for p in prices:
            if cmax < p:
                cmax = p
                m = max(m, cmax - cmin)
            elif cmin > p:
                cmin = p
                cmax = p
        return m