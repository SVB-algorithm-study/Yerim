class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        cur = 0
        for n in nums:
            cur += n
            ans.append(cur)
        return ans