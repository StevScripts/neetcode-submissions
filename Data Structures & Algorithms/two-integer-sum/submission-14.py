class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        target = 7
        seen = [3:0,], holds key,val pairs
        toFind = 7-4

           i
        [3,4,5,6]

        '''

        seen = {}

        for i,v in enumerate(nums):
            diff = target-v
            if diff in seen:
                return [seen[diff],i]
            seen[v] = i
