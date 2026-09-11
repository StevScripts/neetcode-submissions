class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}
        
        for i in range(len(nums)):
            if nums[i] in hMap:
                return True
            
            hMap[nums[i]] = 1
            
        return False