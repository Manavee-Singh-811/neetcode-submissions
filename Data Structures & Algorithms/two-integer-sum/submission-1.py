class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            x = target - nums[i]
            print(x)
            if x in nums[i+1:]:
                j = nums.index(x, i+1)
                return [i,j]

                
        