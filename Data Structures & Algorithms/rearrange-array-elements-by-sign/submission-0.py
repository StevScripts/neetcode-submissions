class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        track the positive and negative,
        then add the next

        '''
        nextP = 0
        nextN = 0
    
        retList = []

        for i in range(len(nums)):
            if i%2 == 0:
                while abs(nums[nextP]) != (nums[nextP]):
                    nextP += 1
                retList.append(nums[nextP])
                nextP += 1

            else:
                while abs(nums[nextN]) == (nums[nextN]):
                    nextN += 1
                retList.append(nums[nextN])
                nextN += 1
        return retList
