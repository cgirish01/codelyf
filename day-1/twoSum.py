def twoSum(nums, target):
        arr={}
        for i, num in enumerate(nums):
            pot_tar= target - num
            if pot_tar in arr:
                return[arr[pot_tar],i]
            else:
                arr[num]=i
        return []

print(twoSum(nums = [2,7,11,15], target=5))