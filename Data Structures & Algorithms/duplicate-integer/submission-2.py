class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Using Sets, Automatically removes duplicates
        #Compare len of nums to nums converted to Sets
        return len(nums) != len(set(nums))
        