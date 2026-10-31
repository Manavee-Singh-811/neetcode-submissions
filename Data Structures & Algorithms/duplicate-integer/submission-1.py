class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if list(set(nums))==nums:
            return False

        return True