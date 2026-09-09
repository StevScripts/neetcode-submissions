class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Loop through with index,val loop
        #find the diff = target - val
        #Make a set with the values we've used
        #If the value is in the set, then we return the indices
        # Set[Diff], v
        #otherwise we add the value to the set and continue with the loop

        pastItems = {}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in pastItems:
                return [pastItems[diff],i]
            pastItems[v] = i
            print(pastItems)
        