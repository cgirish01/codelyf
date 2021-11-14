def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left , right = 0 , len(numbers)-1
        while left<right:
            currentSum =numbers[left]+numbers[right]
            if currentSum==target:
                return[left+1 ,right+1]
            elif currentSum > target:
                right -=1
            elif currentSum < target:
                left+=1
        return[]