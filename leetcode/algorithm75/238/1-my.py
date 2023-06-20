class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        tot = 1
        for n in nums:
            if n != 0:
                tot *= n
                
        zeros = nums.count(0)
        if zeros == 0:
            for i in range(len(nums)):
                ans[i] = tot//nums[i]
        elif zeros == 1:
            ans[nums.index(0)] = tot
        return ans