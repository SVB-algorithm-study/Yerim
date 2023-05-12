class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        def makelst(a):
            savedict = dict()
            savelst = []
            idx = 0
            for i in range(len(a)):
                c = a[i]
                if c not in savedict:
                    savedict[c] = idx
                    idx += 1
                savelst.append(savedict[c])
            return savelst
        
        return makelst(s) == makelst(t)