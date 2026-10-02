class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0

        currCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currCount += 1
            else:
                maxx = max(maxx,currCount)
                currCount = 0
        maxx = max(maxx,currCount)
        return maxx


            
        