class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ans = 0
        d = Counter(s)
        oddExist = False
        for (k, v) in d.items():
            ans += v
            if v%2 == 1:
                ans -= 1
                oddExist = True
        if oddExist:
            ans+=1

        return ans