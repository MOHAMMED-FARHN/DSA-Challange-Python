class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = list(set(nums))
        if len(nums) == len(newlist):
            return False
        return True
        