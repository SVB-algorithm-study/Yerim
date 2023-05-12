class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for e in s:
            if e not in t:
                return False
            t = t[t.index(e)+1:]
        return True