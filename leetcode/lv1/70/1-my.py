class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def comb(a, b):
            nu = de = 1
            for i in range(b, 0, -1):
                nu *= a
                a -= 1
                de *= i
            return nu//de
        
        ans = 0
        for i in range(n//2 +1):
            ans += comb(n-i, i)
        return ans
