class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1,2,3,1

        SubProblem:
        is the sum of the 1st house and cur house better than
        the second house
        '''

    
        rob1,rob2 = 0,0
        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
        