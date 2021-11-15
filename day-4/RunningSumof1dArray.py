def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1:
            return nums
        else:
            for i in range(1,len(nums)):
                nums[i]=nums[i-1]+nums[i]
            return nums