class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def f(cur):
            if cur >= len(nums)-1:
                return True
            for i in range(cur+1, cur+nums[cur]+1):
                if f(i):
                    return True
            return False

        return f(0)