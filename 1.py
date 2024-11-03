class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num1 in range (0, len(nums)-1):
            for num2 in range (1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    if num1 != num2:
                        return [num1, num2]
        
