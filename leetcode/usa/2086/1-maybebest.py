class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        if 'HHH' in hamsters:
            return -1
        if hamsters[:2] == 'HH' or hamsters[-2:] == 'HH' or hamsters == 'H':
            return -1

        ans = hamsters.count('H') - hamsters.count('H.H')
        return ans