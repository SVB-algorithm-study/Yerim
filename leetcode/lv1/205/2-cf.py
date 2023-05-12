class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        sdic = dict()
        tset = set()

        for i in range(len(s)):
            sc, tc = s[i], t[i]
            if sc in sdic:
                if sdic[sc] != tc:
                    return False
            else:
                if tc in tset:
                    return False
                sdic[sc] = tc
                tset.add(tc)
        return True