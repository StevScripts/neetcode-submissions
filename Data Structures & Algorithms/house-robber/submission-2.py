class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1,2,3,1

        SubProblem:
        is the sum of the 1st house and cur house better than
        the second house
        '''

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        houses = [0] * len(nums)
        houses[0], houses[1] = nums[0],max(nums[0],nums[1])
        print(houses)
        for i in range(2,len(nums)):
            houses[i] = max(houses[i-2]+nums[i], houses[i-1])


        return houses[-1]
        