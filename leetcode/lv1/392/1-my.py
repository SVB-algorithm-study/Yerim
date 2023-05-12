class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        si = ti = 0
        while ti < len(t):
            if s[si] == t[ti]:
                si += 1
                if si == len(s):
                    return True
            ti += 1
        return False