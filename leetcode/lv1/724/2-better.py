class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, tot = 0, sum(nums)
        for i in range(len(nums)):
            if left == tot - left - nums[i]:
                return i
            left += nums[i]
        return -1