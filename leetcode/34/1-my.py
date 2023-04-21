class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            ans = [i for (i, x) in enumerate(nums) if x == target]
            return [min(ans), max(ans)]
        else:
            return [-1, -1]