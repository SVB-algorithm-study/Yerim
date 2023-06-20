class Solution(object):
    def climbStairs(self, n):
    #edge cases
        if n<=2: 
           return n
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1], dp[2] = 1, 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]

        return dp[n]