class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in (0,len(nums)):
            x = target - nums[i]
            if x in nums:
                if i!= nums.index(x):
                    return [i, nums.index(x)]
        
        