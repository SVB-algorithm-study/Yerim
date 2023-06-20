# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = 1
        ed = n
        while st < ed:
            i = (st+ed)//2
            if isBadVersion(i):
                ed = i
            else:
                st = i+1
        return ed