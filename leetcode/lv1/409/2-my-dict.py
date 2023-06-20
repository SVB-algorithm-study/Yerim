class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1

        ans = 0
        oddExist = False
        for (k, v) in d.items():
            ans += v
            if v%2 == 1:
                ans -= 1
                oddExist = True
        if oddExist:
            ans+=1
        print(d)
        return ans