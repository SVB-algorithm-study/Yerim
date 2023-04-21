# need better algorithm...

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for r in matrix:
            for e in r:
                if e == target:
                    return True
        return False