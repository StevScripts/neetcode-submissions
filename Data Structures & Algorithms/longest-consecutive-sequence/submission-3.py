class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        set of nums
        check if n-1 exists, if so, disregard
        if it doesnt exist, then start counting upwards checking if n+1 is in the nums set,
        Save the longest

        '''


        longest = 0
        totMax = 0
        seen = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 in seen:
                continue
            
            curVal = nums[i]
            print(curVal)
            while curVal in seen:
                totMax += 1
                curVal += 1
                    
            longest = max(longest,totMax)

            totMax = 0

        
        return longest

            