class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Creating a hashmap and check if target - currentIdx is in the hashmap
        numsDict = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in numsDict:
                return [numsDict[diff],i]
            numsDict[n] = i