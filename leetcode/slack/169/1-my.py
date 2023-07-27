class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = dict()
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] > n//2:
                return nums[i]