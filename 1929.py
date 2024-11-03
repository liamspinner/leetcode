class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range (0, 2):
            for i in range (0, len(nums)):
                arr.append(nums[i])
        
        return arr

        
