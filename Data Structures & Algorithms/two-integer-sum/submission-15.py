class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''


        target = 7

        [3,4,5,6]


        target - item = itemToFind
        if itemToFind in nums:
            return [item,nums[index]]
        '''

        hMap = {}

        for i,v in enumerate(nums):
            toFind = target-v
            if toFind in hMap:
                return [hMap[toFind],i]
            hMap[v] = i
