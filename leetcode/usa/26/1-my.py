class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        idx = 0
        for i in range(len(nums)):
            if nums[i] not in s:
                nums[idx] = nums[i]
                idx += 1
                s.add(nums[i])
        return idx